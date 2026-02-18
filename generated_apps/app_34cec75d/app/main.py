import csv
from typing import List
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    data: List[List[str]] = list(reader)
print(len(data))