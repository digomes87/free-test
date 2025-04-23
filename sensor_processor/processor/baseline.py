from typing import List

from numpy import mean
from .base import SensorDataProcessor


class BaselineProcessor(SensorDataProcessor):
    @staticmethod
    def calculate_mean(values: List[float]) -> float:
        if not values:
            return 0.0
        return sum(values) / len(values)

    @staticmethod
    def calculate_standard_deviation(values: List[float]) -> float:
        if not values:
            return 0.0

        mean = BaselineProcessor.calculate_mean(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return variance**0.5

    @staticmethod
    def calculate_moving_average(
        values: List[float], window_size: int = 5
    ) -> List[float]:
        if window_size <= 0 or window_size > len(values):
            return []
        return [
            sum(values[i : i + window_size]) / window_size
            for i in range(len(values) - window_size + 1)
        ]
