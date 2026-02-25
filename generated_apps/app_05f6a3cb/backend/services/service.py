from backend.db.db import DB
class Service:
    def __init__(self):
        self.db = DB()
    def read_all_items(self):
        return self.db.get_all_items()
    def create_item(self, item: dict):
        self.db.save_item(item)
