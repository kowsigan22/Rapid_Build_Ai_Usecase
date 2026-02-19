from fastapi import FastAPI
from backend.controllers.main import app
from backend.db.main import InMemoryDatabase
class Service:
    def __init__(self):
        self.app = app
        self.db = InMemoryDatabase()
    def get_items(self) -> List[Dict]:
        return self.db.get_items()
    def create_item(self, item: Dict):
        self.db.add_item(item)
