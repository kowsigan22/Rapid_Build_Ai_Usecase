import csv
from typing import TextIO
with open('input.csv', 'r') as f:
    reader = csv.reader(f)
    count = sum(1 for _ in reader)
print(count)
