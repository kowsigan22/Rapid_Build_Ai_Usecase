import csv
from typing import TextIO
with open('input.csv', 'r') as f:
    reader = csv.reader(f)
    print(len(list(reader)))
