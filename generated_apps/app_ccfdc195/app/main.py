import csv
from typing import Dict

def load_data(file_path: str) -> int:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return sum(1 for _ in reader)

if __name__ == '__main__':
    data_file = 'data.csv'
    row_count = load_data(data_file)
    print(row_count)
