import csv
from typing import Dict
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    data: Dict[str, list] = [row for row in reader]
print(len(data))
