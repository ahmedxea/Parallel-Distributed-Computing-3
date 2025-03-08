import time
from tqdm import tqdm
from skimage.filters.rank import entropy
from skimage.morphology import disk
from scipy import ndimage as nd
from skimage.filters import sobel, gabor, hessian, prewitt
from src.data_loader import load_dataset

def apply_filters(image):
    """
    Applies multiple filters to a single image.
    
    Returns:
        - dict: Dictionary of filtered images.
    """
    return {
        'Original': image,
        'Entropy': entropy(image, disk(2)),
        'Gaussian': nd.gaussian_filter(image, sigma=1),
        'Sobel': sobel(image),
        'Gabor': gabor(image, frequency=0.9)[1],
        'Hessian': hessian(image, sigmas=range(1, 100, 1)),
        'Prewitt': prewitt(image)
    }

def process_images(images):
    """
    Applies filters sequentially to images.
    
    Returns:
        - list: List of dictionaries containing filtered images.
    """
    processed_images = []
    for image in tqdm(images[:5]):  # Process first 5 images for testing
        processed_images.append(apply_filters(image))

    return processed_images
