from backend.db import InMemoryDatabase
class ItemService:
    def __init__(self):
        self.db = InMemoryDatabase()
    def read_items(self):
        return [Item(name="Item 1", description="Description 1"), Item(name="Item 2", description="Description 2")]