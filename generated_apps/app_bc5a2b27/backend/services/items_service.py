from typing import List
from backend.db.in_memory_db import InMemoryDB
class ItemsService:
    def __init__(self):
        self.db = InMemoryDB()
    def read_items(self) -> List[dict]:
        return [item.__dict__ for item in self.db.get_all_items()]