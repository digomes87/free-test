import numpy as np
from processor.utils import generator_sensor_data, print_processing_results
from processor.baseline import BaselineProcessor
from processor.numpy_impl import NumpyProcessor
from processor.processor_runner import process_sensor_data


def main():
    print("Generating sensor data ...")
    data = generator_sensor_data()
    raw_values = [v for _, v in data]
    raw_array = np.array(raw_values)

    print("Running Baseline")
    result = process_sensor_data(BaselineProcessor, raw_values)
    print_processing_results("Baseline", *result)

    print("Running Numpy...")
    result = process_sensor_data(NumpyProcessor, raw_array)
    print_processing_results("Numpy", *result)


if __name__ == "__main__":
    main()
