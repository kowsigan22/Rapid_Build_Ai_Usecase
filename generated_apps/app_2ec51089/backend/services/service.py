from backend.db import DB
class Service:
    def get_all_items(self):
        return DB.items
    def create_item(self, item: dict):
        DB.items.append(item)
