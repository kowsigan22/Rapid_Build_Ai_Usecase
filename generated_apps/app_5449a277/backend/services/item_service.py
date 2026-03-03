from .db import InMemoryDatabase
class ItemService:
    def __init__(self):
        self.db = InMemoryDatabase()
    def read_items(self):
        return self.db.get_all_items()
    def create_item(self, item: dict):
        self.db.add_item(item)
