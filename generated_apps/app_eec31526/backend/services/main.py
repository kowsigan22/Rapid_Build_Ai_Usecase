from backend.db import InMemoryDatabase
from typing import List, Dict
class Service:
    def __init__(self):
        self.db = InMemoryDatabase()
    def get_items(self) -> List[Dict]:
        return self.db.get_items()
    def create_item(self, item: Dict) -> None:
        self.db.add_item(item)
