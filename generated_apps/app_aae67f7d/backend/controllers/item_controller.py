from fastapi import Response
from backend.services.service_layer import service
from backend.db.db_layer import db
class ItemController:
    def read_items(self):
        items = [{}]
        return items
    def create_item(self, item: dict):
        db.insert(item)
        return item