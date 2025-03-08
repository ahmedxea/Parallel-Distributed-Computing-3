import cv2
import numpy as np
from skimage import exposure

def load_image(image_path):
    """Loads an image from a file."""
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError(f"Image at {image_path} could not be loaded.")
    return image

def preprocess_image(image):
    """Applies preprocessing steps such as resizing, normalization, and histogram equalization."""
    image = cv2.resize(image, (128, 128))  # Resize to a fixed size
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    image = exposure.equalize_hist(image)  # Histogram equalization
    return image

def normalize_image(image):
    """Normalizes pixel values between 0 and 1."""
    return image / 255.0
