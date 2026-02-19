from backend.controllers.items import router
from backend.db.memory_db import MemoryDB
class Service:
    def __init__(self):
        self.memory_db = MemoryDB()
    def get_items(self):
        return self.memory_db.get_items()
    def store_item(self, item):
        self.memory_db.store_item(item)
