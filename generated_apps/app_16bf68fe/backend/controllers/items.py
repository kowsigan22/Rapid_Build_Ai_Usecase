from typing import List
from backend.services.items import ItemsService
class ItemsController:
    def __init__(self):
        self.service = ItemsService()
    def get_all_items(self):
        return self.service.get_all_items()
    def create_item(self, item: dict):
        return self.service.create_item(item)
