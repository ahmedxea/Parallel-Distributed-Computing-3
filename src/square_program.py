import time
import random
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

# Function to compute the square of a number
def square(n):
    return n * n

# Generate lists of numbers (10^6 and 10^7)
N1 = 10**6  # 1 million numbers
N2 = 10**7  # 10 million numbers
numbers_1 = [random.randint(1, 1000) for _ in range(N1)]
numbers_2 = [random.randint(1, 1000) for _ in range(N2)]


# 1. Sequential Execution
def sequential_execution(numbers):
    """Computes squares sequentially using a for loop."""
    start = time.time()
    result = [square(n) for n in numbers]
    end = time.time()
    print(f"Sequential Execution Time ({len(numbers)} numbers): {end - start:.4f} sec")
    return result


# 2. Multiprocessing with Individual Processes
def square_worker(n, output_list):
    """Worker function to compute square and store in shared list"""
    output_list.append(square(n))

def multiprocessing_individual(numbers):
    """Creates a separate process for each number (inefficient)."""
    start = time.time()
    manager = multiprocessing.Manager()
    output_list = manager.list()
    processes = []

    for num in numbers:
        p = multiprocessing.Process(target=square_worker, args=(num, output_list))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    end = time.time()
    print(f"Multiprocessing (Individual Processes) Execution Time ({len(numbers)} numbers): {end - start:.4f} sec")
    return output_list


# 3. Multiprocessing Pool (map)
def multiprocessing_pool_map(numbers):
    """Uses multiprocessing Pool.map to parallelize squaring."""
    start = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = pool.map(square, numbers)
    end = time.time()
    print(f"Multiprocessing Pool (map) Execution Time ({len(numbers)} numbers): {end - start:.4f} sec")
    return result


# 4. Multiprocessing Pool (apply)
def multiprocessing_pool_apply(numbers):
    """Uses multiprocessing Pool.apply (less efficient than map)."""
    start = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result = [pool.apply(square, args=(n,)) for n in numbers]
    end = time.time()
    print(f"Multiprocessing Pool (apply) Execution Time ({len(numbers)} numbers): {end - start:.4f} sec")
    return result


# 5. Using concurrent.futures ProcessPoolExecutor
def process_pool_executor(numbers):
    """Uses concurrent.futures for parallel execution."""
    start = time.time()
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        result = list(executor.map(square, numbers))
    end = time.time()
    print(f"ProcessPoolExecutor Execution Time ({len(numbers)} numbers): {end - start:.4f} sec")
    return result

if __name__ == "__main__":
    print("\n### Running tests with 10^6 numbers ###")
    sequential_execution(numbers_1)
    multiprocessing_individual(numbers_1)
    multiprocessing_pool_map(numbers_1)
    multiprocessing_pool_apply(numbers_1)
    process_pool_executor(numbers_1)

    print("\n### Running tests with 10^7 numbers ###")
    sequential_execution(numbers_2)
    multiprocessing_pool_map(numbers_2)
    process_pool_executor(numbers_2)
