from typing import List, Union
import numpy as np


NumericSequence = Union[List[float], np.ndarray]


class SensorDataProcessor:
    @staticmethod
    def calculate_mean(values: NumericSequence) -> float:
        raise NotImplementedError

    @staticmethod
    def calculate_standard_deviation(values: NumericSequence) -> float:
        raise NotImplementedError

    @staticmethod
    def calculate_moving_average(values: NumericSequence, window_size: int = 5) -> List:
        raise NotImplementedError
