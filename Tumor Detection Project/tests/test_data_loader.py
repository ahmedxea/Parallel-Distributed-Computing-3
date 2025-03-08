import unittest
from src.data_loader import load_dataset

class TestDataLoader(unittest.TestCase):
    def test_load_dataset(self):
        dataset_path = "data/"
        yes_images, no_images = load_dataset(dataset_path)

        self.assertGreater(len(yes_images), 0, "No tumor images loaded!")
        self.assertGreater(len(no_images), 0, "No non-tumor images loaded!")

if __name__ == "__main__":
    unittest.main()
