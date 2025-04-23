import numpy as np
from .base import SensorDataProcessor


class NumpyProcessor(SensorDataProcessor):
    @staticmethod
    def calculate_mean(values: np.ndarray) -> float:
        return float(np.mean(values)) if values.size > 0 else 0.0

    @staticmethod
    def calculate_standard_deviation(values: np.ndarray) -> float:
        return float(np.std(values)) if values.size > 0 else 0.0

    @staticmethod
    def calculate_moving_average(values: np.ndarray, window_size: int = 5) -> list:
        if window_size <= 0 or window_size > len(values):
            return []
        kernel = np.ones(window_size) / window_size
        return np.convolve(values, kernel, mode="valid").tolist()
