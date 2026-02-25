from backend.db.db_layer import db
class ServiceLayer:
    def read_items(self):
        return db.read()
    def create_item(self, item: dict):
        db.insert(item)
