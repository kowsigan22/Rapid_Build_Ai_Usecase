from typing import List, Dict
from backend.models.item import Item
class Database:
    def __init__(self):
        self.items: List[Dict] = []

    def get_items(self) -> List[Item]:
        return [Item(**item) for item in self.items]

    def add_item(self, item: Item):