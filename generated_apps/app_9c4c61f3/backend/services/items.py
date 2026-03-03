from backend.db.database import Database
class ItemsService:
    def __init__(self, db: Database):
        self.db = db
    def get(self):
        return self.db.get_items()
    def post(self, item: Item):
        self.db.store_item(item)
