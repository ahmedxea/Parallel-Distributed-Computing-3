from mpi4py import MPI
import numpy as np
import socket

# Step 1: Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
hostname = socket.gethostname()

# Step 2: Parameters
population_size = 100
spread_chance = 0.3
vaccination_rate = np.random.uniform(0.1, 0.5)

# Step 3: Initialize local population
local_size = population_size // size
population = np.zeros(local_size, dtype=int)

# Infect 10% randomly on root process, then scatter
if rank == 0:
    full_population = np.zeros(population_size, dtype=int)
    infected_indices = np.random.choice(population_size, int(0.1 * population_size), replace=False)
    full_population[infected_indices] = 1
    chunks = np.array_split(full_population, size)
else:
    chunks = None

# Distribute population chunks to all processes
population = comm.scatter(chunks, root=0)

# Step 4: Virus spread function
def spread_virus(pop, spread_chance, vaccination_rate):
    new_pop = pop.copy()
    for i in range(len(pop)):
        if pop[i] == 0:  # not infected
            if np.random.rand() < spread_chance * (1 - vaccination_rate):
                new_pop[i] = 1
    return new_pop

# Step 5: Run simulation
for _ in range(10):
    population = spread_virus(population, spread_chance, vaccination_rate)

# Step 6: Gather final populations
all_populations = comm.gather(population, root=0)

# Step 7: Final infection rate
if rank == 0:
    full_population = np.concatenate(all_populations)
    total_infected = np.sum(full_population)
    infection_rate = total_infected / population_size
    print(f"[Root] Infection Rate = {infection_rate:.2f}")
else:
    print(f"Process {rank} on {hostname}: Local Vaccination Rate = {vaccination_rate:.2f}")
