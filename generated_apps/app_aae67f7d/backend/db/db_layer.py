from typing import List
from backend.models import Item
class DB:
    items: List[Item] = []
    def read(self):
        return self.items
    def insert(self, item: dict):
        self.items.append(Item(**item))