from backend.db import ItemDB
class ItemService:
    def __init__(self):
        self.item_db = ItemDB()
    def read_items(self):
        return self.item_db.get_all_items()