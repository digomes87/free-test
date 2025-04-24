import unittest
from processor.baseline import BaselineProcessor
from processor.utils import generator_sensor_data


class TesteBaseLineProcessor(unittest.TestCase):

    def test_calculate_mean(self):
        values = [1, 2, 3, 4, 5]
        self.assertEqual(BaselineProcessor.calculate_mean(values), 3.0)


    def test_calculate_standart_deviation(self):
        values = [ 2, 4, 4, 4, 5 ,5, 7, 9]
        std = BaselineProcessor.calculate_standard_deviation(values)
        self.assertAlmostEqual(std, 2.0, places=1)

    
    def test_calculate_moving_average(self):
        values = [1, 2, 3, 4, 5, 6]
        expected = [2.0, 3.0, 4.0, 5.0]
        result = BaselineProcessor.calculate_moving_average(values, window_size=3)
        self.assertEqual(result, expected)


class TestUtils(unittest.TestCase):

    def test_generate_sensor_data(self):
        num_records = 10
        data = generator_sensor_data(num_records)
        self.assertEqual(len(data), num_records)
        for timestamp, value in data:
            self.assertIsInstance(timestamp, float)
            self.assertIsInstance(value, float)


if __name__ == "__main__":
    unittest.main()
