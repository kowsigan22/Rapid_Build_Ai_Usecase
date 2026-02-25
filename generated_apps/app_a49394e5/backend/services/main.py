from backend.controllers.main import app
from backend.db.in_memory_db import InMemoryDB

class Service:
    def __init__(self, db: InMemoryDB):
        self.db = db

    def get_items(self):
        return self.db.get_items()

    def create_item(self, item: dict):
        self.db.add_item(item)
