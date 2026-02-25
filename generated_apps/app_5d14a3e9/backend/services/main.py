from backend.controllers.main import app
from backend.db.in_memory_db import InMemoryDB
class Service:
    def __init__(self):
        self.db = InMemoryDB()
    def get_items(self):
        return self.db.get_items()
    def create_item(self, item):
        self.db.add_item(item)
