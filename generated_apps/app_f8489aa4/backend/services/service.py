from backend.db.database import database
class Service:
    def __init__(self):
        self.db = database()
    def get_items(self):
        return self.db.items
    def create_item(self, item: dict):
        self.db.items.append(item)
