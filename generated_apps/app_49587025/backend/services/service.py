from .db import Database
class Service:
    def __init__(self, db: Database):
        self.db = db
    def read_items(self):
        return self.db.get_all_items()
    def create_item(self, item: dict):
        self.db.save_item(item)
