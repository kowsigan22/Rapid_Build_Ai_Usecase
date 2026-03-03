from backend.db import InMemoryDatabase
from backend.models import Item
class ItemService:
    def get_items(self):
        return [Item(name="Item 1"), Item(name="Item 2")]