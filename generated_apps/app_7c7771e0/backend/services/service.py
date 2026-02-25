from backend.db.db import Database
from backend.models.item import Item
class Service:
    def __init__(self, item: dict):
        self.item = Item(**item)
    def get_items(self) -> List[dict]:
        return Database().get_items()
    def create_item(self, request: dict) -> dict:
        return Database().create_item(request)