import unittest
import numpy as np
from src.feature_extraction import compute_glcm_features

class TestFeatureExtraction(unittest.TestCase):
    def test_feature_extraction(self):
        test_image = np.random.rand(128, 128)  # Simulated grayscale image
        features = compute_glcm_features(test_image, "TestFilter")

        self.assertTrue(isinstance(features, dict), "Feature extraction did not return a dictionary!")
        self.assertGreater(len(features), 0, "No features extracted!")

if __name__ == "__main__":
    unittest.main()
