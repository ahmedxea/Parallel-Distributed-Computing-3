import time
from src.data_loader import load_dataset
from src.sequential_filtering import process_images
from src.parallel_filtering import parallel_execution

# Load dataset
dataset_path = "data/"
yes_images, no_images = load_dataset(dataset_path)

# Run sequential execution
print("\nRunning Sequential Execution...")
sequential_start = time.time()
yes_inputs_seq = process_images(yes_images)
no_inputs_seq = process_images(no_images)
sequential_end = time.time()
sequential_time = sequential_end - sequential_start
print(f"Sequential Execution Time: {sequential_time:.2f} sec")

# Run parallel execution
print("\nRunning Parallel Execution...")
parallel_start = time.time()
yes_inputs_par = parallel_execution(yes_images)
no_inputs_par = parallel_execution(no_images)
parallel_end = time.time()
parallel_time = parallel_end - parallel_start
print(f"Parallel Execution Time: {parallel_time:.2f} sec")

# Compute speedup
speedup = sequential_time / parallel_time
print(f"\nSpeedup: {speedup:.2f}x")
