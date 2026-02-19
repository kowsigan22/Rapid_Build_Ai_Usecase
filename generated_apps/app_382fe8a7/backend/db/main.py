from typing import List, Dict
from backend.models.main import Item
class DB:
    def __init__(self):
        self.items: List[Item] = []

    def get_items(self) -> List[Item]:
        return self.items

    def add_item(self, item: Item) -> Item:
        self.items.append(item)
        return item
