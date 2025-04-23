from typing import List, Tuple
import numpy as np


SensorRecord = Tuple[int, float, float, float]


def generator_sensor_data(n_samples: int = 1_000_000) -> List[SensorRecord]:
    timestamps = np.arange(n_samples)
    sensor_1 = np.random.normal(loc=0.0, scale=1.0, size=n_samples)
    sensor_2 = np.random.normal(loc=10.0, scale=5.0, size=n_samples)
    sensor_3 = np.random.normal(loc=5.0, scale=2.0, size=n_samples)

    return list(zip(timestamps, sensor_1, sensor_2, sensor_3))
