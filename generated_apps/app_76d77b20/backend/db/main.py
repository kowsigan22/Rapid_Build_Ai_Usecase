from typing import List
from backend.models.item import Item
class Database:
    def __init__(self):
        self.items: List[Item] = [Item(id=1, name="Item 1", description="Description 1"), Item(id=2, name="Item 2", description="Description 2")]
    def get_items(self):
        return self.items
    def create_item(self, item: Item):
        self.items.append(item)
