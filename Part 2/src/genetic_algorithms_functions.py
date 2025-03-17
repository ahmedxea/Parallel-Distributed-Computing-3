import numpy as np

def calculate_fitness(route, distance_matrix):
    """
    Calculates total distance for a given route.

    Parameters:
        - route (list): A list representing the order of nodes visited.
        - distance_matrix (numpy.ndarray): Distance matrix of the graph.

    Returns:
        - float: The negative total distance traveled.
    """
    total_distance = 0
    for i in range(len(route) - 1):
        node1, node2 = route[i], route[i + 1]
        distance = distance_matrix[node1][node2]

        # Apply a penalty for infeasible routes
        if distance == 100000:
            total_distance += 500

        total_distance += distance

    return -total_distance  # Negative because we minimize distance


def select_in_tournament(population, scores, number_tournaments=4, tournament_size=3):
    """
    Tournament selection.

    Parameters:
        - population (list): The current population.
        - scores (np.array): Fitness scores for the population.
        - number_tournaments (int): Number of tournaments.
        - tournament_size (int): Number of individuals competing in each tournament.

    Returns:
        - list: Selected individuals for crossover.
    """
    selected = []
    
    for _ in range(number_tournaments):
        idx = np.random.choice(len(population), tournament_size, replace=False)
        best_idx = idx[np.argmin(scores[idx])]
        selected.append(population[best_idx])

    return selected


def order_crossover(parent1, parent2):
    """
    Order crossover (OX) for permutations.

    Parameters:
        - parent1 (list): First parent route.
        - parent2 (list): Second parent route.

    Returns:
        - list: Offspring route.
    """
    size = len(parent1)
    start, end = sorted(np.random.choice(range(size), 2, replace=False))
    
    offspring = [None] * size
    offspring[start:end + 1] = parent1[start:end + 1]
    
    fill_values = [x for x in parent2 if x not in offspring[start:end + 1]]
    
    idx = 0
    for i in range(size):
        if offspring[i] is None:
            offspring[i] = fill_values[idx]
            idx += 1
    
    return offspring


def mutate(route, mutation_rate):
    """
    Mutation operator: Swap two nodes in the route.
    
    - If stagnation is high, increase mutation probability.
    """
    if np.random.rand() < mutation_rate:
        i, j = np.random.choice(len(route), 2, replace=False)
        route[i], route[j] = route[j], route[i]
    return route



def generate_unique_population(population_size, num_nodes):
    """
    Generates a unique population of routes.

    Parameters:
        - population_size (int): Number of individuals in the population.
        - num_nodes (int): Number of nodes in the graph.

    Returns:
        - list of lists: A list of unique routes.
    """
    population = set()
    while len(population) < population_size:
        individual = [0] + list(np.random.permutation(np.arange(1, num_nodes)))
        population.add(tuple(individual))
    return [list(ind) for ind in population]
