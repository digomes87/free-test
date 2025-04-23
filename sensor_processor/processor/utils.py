import numpy as np
from typing import List, Tuple


def generator_sensor_data(num_records: int = 1000) -> List[Tuple[float, float]]:
    return [(i * 0.1, np.random.normal(50, 10)) for i in range(num_records)]


def print_processing_results(
    name: str, mean: float, std_dev: float, mov_avg: List[float], exec_time: float
) -> None:
    print(f"\n{name} Results:")
    print(f"- Mean: {mean:.4f}")
    print(f"- Standard Deviation: {std_dev:.4f}")
    print(f"- First 5 moving average values: {mov_avg}")
    print(f"- Execution time: {exec_time} seconds")
