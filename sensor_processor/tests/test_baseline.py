import unittest
import numpy as np
from processor.numpy_impl import NumpyProcessor
# from processor.baseline import generator_sensor_data


class TestNumpyProcessor(unittest.TestCase):
    def setUp(self):
        # Garante que os dados sejam reprodutíveis
        np.random.seed(42)
        self.values = np.random.normal(loc=50, scale=10, size=1000)
    
    def test_calculate_mean_within_expected_range(self):
        mean = NumpyProcessor.calculate_mean(self.values)
        self.assertTrue(45 <= mean <= 55, f"Mean out of expected range: {mean}")

    def test_calculate_standard_deviation_reasonable(self):
        std = NumpyProcessor.calculate_standard_deviation(self.values)
        self.assertTrue(8 <= std <= 12, f"Std dev out of expected range: {std}")

    def test_calculate_moving_average_length(self):
        result = NumpyProcessor.calculate_moving_average(self.values, window_size=50)
        expected_length = len(self.values) - 50 + 1
        self.assertEqual(len(result), expected_length)
        self.assertIsInstance(result, list)


# class TestUtils(unittest.TestCase):
#
#     def test_generate_sensor_data(self):
#         num_records = 10
#         data = generator_sensor_data(num_records)
#         self.assertEqual(len(data), num_records)
#         for timestamp, value in data:
#             self.assertIsInstance(timestamp, float)
#             self.assertIsInstance(value, float)


if __name__ == "__main__":
    unittest.main()
