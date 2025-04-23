import time
from .base import SensorDataProcessor


def process_sensor_data(processor: SensorDataProcessor, values, window_size: int = 50):
    start = time.perf_counter()
    mean = processor.calculate_mean(values)
    std_dev = processor.calculate_standard_deviation(values)
    mov_avg = processor.calculate_moving_average(values, window_size)
    elapsed = time.perf_counter() - start
    return mean, std_dev, mov_avg, elapsed
