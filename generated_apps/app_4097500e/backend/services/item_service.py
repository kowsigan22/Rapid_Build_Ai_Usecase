from backend.db import InMemoryDatabase
class ItemService:
    def __init__(self):
        self.db = InMemoryDatabase()
    def read_items(self):
        return [Item(name="item1", description="desc1"), Item(name="item2", description="desc2")]