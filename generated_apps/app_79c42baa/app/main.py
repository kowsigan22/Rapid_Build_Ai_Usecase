import csv
from typing import Dict
from pathlib import Path
def main():
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        count = sum(1 for _ in reader)
        print(count)
if __name__ == '__main__':
    main()
