from backend.db import InMemoryDatabase
from backend.models import Item
class ItemService:
    def __init__(self):
        self.db = InMemoryDatabase()
    def read_items(self):
        return [Item(name="Item 1"), Item(name="Item 2")]