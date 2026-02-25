from backend.db.database import Database
from pydantic import BaseModel

class Service:
    def __init__(self):
        self.db = Database()

    def get_items(self):
        return self.db.get_items()

    def add_item(self, item: dict):
        self.db.add_item(Item(**item))