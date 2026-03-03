from backend.db import ItemDatabase
class ItemService:
    def __init__(self, db: ItemDatabase):
        self.db = db
    def read_items(self):
        return self.db.get_all_items()
    def create_item(self, item: dict):
        self.db.save_item(item)
