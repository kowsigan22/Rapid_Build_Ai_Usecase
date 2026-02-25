from backend.db.db import DB
class Service:
    def __init__(self, db: DB):
        self.db = db

    def get_items(self):
        return self.db.get_all_items()

    def create_item(self, item: dict):
        self.db.create_item(item)
