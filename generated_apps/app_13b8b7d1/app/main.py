import csv
from typing import TextIO
def load_csv(file_path: str) -> int:
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return sum(1 for _ in reader)
if __name__ == '__main__':
    print(load_csv('data.csv'))