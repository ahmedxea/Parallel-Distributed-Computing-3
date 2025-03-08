from multiprocessing import Pool, cpu_count
import numpy as np
import skimage.feature as feature


def compute_glcm_features(image, filter_name):
    """
    Computes GLCM features for an image.

    Parameters:
        - image (numpy.ndarray): Image to process.
        - filter_name (str): Name of the filter applied.

    Returns:
        - dict: Extracted GLCM features.
    """
    image = (image * 255).astype(np.uint8)
    graycom = feature.graycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)

    features = {}
    for prop in ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM']:
        values = feature.graycoprops(graycom, prop).flatten()
        for i, value in enumerate(values):
            features[f'{filter_name}_{prop}_{i+1}'] = value
    return features
