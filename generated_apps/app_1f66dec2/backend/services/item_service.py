from backend.db.in_memory_db import db_instance

class ItemService:

    def get_items(self):
        return db_instance.get_all()

    def create_item(self, item):
        return db_instance.add(item)
