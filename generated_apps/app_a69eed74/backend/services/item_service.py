from backend.db import InMemoryDatabase
class ItemService:
    def read_items(self):
        return self.db.get_all_items()
    def create_item(self, item: dict):
        self.db.add_item(item)
        return item
