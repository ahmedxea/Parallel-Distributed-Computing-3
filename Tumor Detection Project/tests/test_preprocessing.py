import unittest
import numpy as np
from src.preprocessing import load_image, preprocess_image, normalize_image

class TestPreprocessing(unittest.TestCase):
    def test_preprocessing(self):
        image_path = "data/yes/image1.jpg"  # Change this to an actual image path
        image = load_image(image_path)
        processed_image = preprocess_image(image)
        normalized_image = normalize_image(processed_image)

        self.assertEqual(processed_image.shape, (128, 128), "Resized image shape incorrect!")
        self.assertTrue(np.all((normalized_image >= 0) & (normalized_image <= 1)), "Normalization failed!")

if __name__ == "__main__":
    unittest.main()
