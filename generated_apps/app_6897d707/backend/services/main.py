from backend.db.in_memory_database import InMemoryDatabase
from pydantic import BaseModel

class Service:
    def __init__(self):
        self.db = InMemoryDatabase()

    def get_items(self):
        return self.db.get_items()

    def add_item(self, item: dict):
        self.db.add_item(item)
