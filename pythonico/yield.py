import sys


def read_data(file_name):
    with open(file_name, "r") as file:
        return file.readlines()

def read_data_with_yield(file_name):
    with open(file_name, "r") as file:
        for line in file:
            yield line


data = read_data_with_yield("customers.csv")
size = sys.getsizeof(data)

print(f"Tamanho do arquivo: {size}")
print(*data, sep="")
print(size)
