from backend.db import in_memory_db
class ItemService:
    def read_items(self):
        return in_memory_db.get_all_items()
    def create_item(self, item: dict):
        in_memory_db.add_item(item)
        return item
