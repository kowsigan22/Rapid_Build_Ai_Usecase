from typing import List
from backend.db.items import ItemsDB
class ItemsService:
    def __init__(self):
        self.db = ItemsDB()
    def get_all_items(self):
        return self.db.get_all_items()
    def create_item(self, item: dict):
        self.db.create_item(item)
