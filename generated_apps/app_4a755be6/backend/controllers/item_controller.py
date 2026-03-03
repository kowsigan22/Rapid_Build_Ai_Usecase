from fastapi import HTTPException
from backend.models import Item
class ItemController:
    def get(self):
        return [Item(name="Item 1"), Item(name="Item 2")]