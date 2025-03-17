from mpi4py import MPI
import numpy as np
import pandas as pd
import os
import time
from genetic_algorithms_functions import calculate_fitness, \
    select_in_tournament, order_crossover, mutate, \
    generate_unique_population
 
# MPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Start timing
start_time = time.time() if rank == 0 else None

# Load distance matrix (only on root process)
if rank == 0:
    file_path = os.path.join(os.path.dirname(__file__), '../data/city_distances.csv')
    distance_matrix = pd.read_csv(file_path).to_numpy()
    num_nodes = distance_matrix.shape[0]
    population_size = 10000
    num_generations = 200
    mutation_rate = 0.1
    stagnation_limit = 15  # Increased stagnation limit

    # Generate initial population
    np.random.seed(42)
    population = generate_unique_population(population_size, num_nodes)

else:
    distance_matrix = None
    num_nodes = None
    population = None

# Broadcast shared variables to all processes
distance_matrix = comm.bcast(distance_matrix, root=0)
num_nodes = comm.bcast(num_nodes, root=0)

# Ensure population is split correctly before scattering
if rank == 0:
    chunk_size = population_size // size
    chunks = [population[i * chunk_size:(i + 1) * chunk_size] for i in range(size)]
else:
    chunks = None

# Scatter population to all processes
local_population = comm.scatter(chunks, root=0)

best_fitness = float('inf')
stagnation_counter = 0

# Main GA loop
for generation in range(num_generations):
    # Calculate fitness in parallel
    local_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in local_population])
    
    # Gather fitness values from all processes
    all_fitness_values = comm.gather(local_fitness_values, root=0)

    if rank == 0:
        all_fitness_values = np.concatenate(all_fitness_values)
        best_generation_fitness = np.min(all_fitness_values)

        if best_generation_fitness < best_fitness:
            best_fitness = best_generation_fitness
            stagnation_counter = 0
        else:
            stagnation_counter += 1

        # Dynamic mutation increase on stagnation
        if stagnation_counter >= stagnation_limit:
            print(f"Regenerating population at generation {generation} due to stagnation")
            mutation_rate = min(0.5, mutation_rate * 1.2)  # Increase mutation rate dynamically
            population = generate_unique_population(population_size, num_nodes)
            stagnation_counter = 0
        else:
            # Selection and crossover
            selected = select_in_tournament(population, all_fitness_values, tournament_size=5)
            offspring = []
            for i in range(0, len(selected), 2):
                parent1, parent2 = selected[i], selected[i + 1]
                route1 = order_crossover(parent1[1:], parent2[1:])
                offspring.append([0] + route1)
            mutated_offspring = [mutate(route, mutation_rate) for route in offspring]

            # Replacement in population
            for i, idx in enumerate(np.argsort(all_fitness_values)[::-1][:len(mutated_offspring)]):
                population[idx] = mutated_offspring[i]

        # Redistribute updated population
        chunks = [population[i * chunk_size:(i + 1) * chunk_size] for i in range(size)]
    else:
        chunks = None

    # Scatter updated population back to processes
    local_population = comm.scatter(chunks, root=0)

# Gather final population at rank 0
final_population = comm.gather(local_population, root=0)

if rank == 0:
    final_population = np.concatenate(final_population)
    final_fitness_values = np.array([calculate_fitness(route, distance_matrix) for route in final_population])

    best_idx = np.argmin(final_fitness_values)
    best_solution = final_population[best_idx]

    # End timing
    end_time = time.time()
    print("Best Solution:", list(map(int, best_solution)))
    print("Total Distance:", calculate_fitness(best_solution, distance_matrix))
    print(f"Execution Time: {end_time - start_time:.2f} seconds")
