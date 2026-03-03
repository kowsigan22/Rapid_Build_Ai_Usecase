from backend.db.database import Database
class ItemsService:
    def __init__(self, db: Database):
        self.db = db
    def get_items(self):
        return self.db.get_items()
    def store_item(self, item: dict):
        self.db.store_item(item)
