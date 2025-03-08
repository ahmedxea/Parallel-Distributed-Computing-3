import glob
import cv2
import numpy as np

def read_images(image_paths):
    """
    Reads all images from a specified path using OpenCV.

    Parameters:
        - image_paths (list): List of image file paths.

    Returns:
        - images (list): List of grayscale images.
    """
    images = []
    for file_path in image_paths:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            images.append(image)
        else:
            print(f"Warning: Failed to load {file_path}")
    return images

def load_dataset(dataset_path):
    """
    Loads MRI images from 'yes' and 'no' folders.

    Returns:
        - yes_images (list): Images containing tumors.
        - no_images (list): Images without tumors.
    """
    yes_images = glob.glob(f"{dataset_path}/yes/*.jpg")
    no_images = glob.glob(f"{dataset_path}/no/*.jpg")

    yes_images = read_images(yes_images)
    no_images = read_images(no_images)

    print(f"Loaded {len(yes_images)} tumor images and {len(no_images)} non-tumor images.")
    return yes_images, no_images
