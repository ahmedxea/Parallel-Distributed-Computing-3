import time
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
from src.sequential_filtering import apply_filters
from src.data_loader import load_dataset

def parallel_execution(images):
    """
    Applies filters in parallel using multiprocessing.

    Parameters:
        - images (list): List of grayscale images.

    Returns:
        - list: List of dictionaries containing filtered images.
    """
    start_time = time.time()
    
    with Pool(processes=cpu_count()) as pool:
        filtered_images = list(tqdm(pool.imap(apply_filters, images[:5]), total=len(images[:5])))

    end_time = time.time()
    print(f"Parallel Execution Time: {end_time - start_time:.2f} sec")

    return filtered_images
