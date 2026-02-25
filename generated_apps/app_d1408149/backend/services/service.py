from backend.db.database import Database
class Service:
    def __init__(self):
        self.db = Database()
    def get_all_items(self):
        return self.db.get_all_items()
    def create_item(self, item: dict):
        return self.db.create_item(item)