from fastapi import APIRouter
from backend.services import Service

router = APIRouter()

class ItemController:
    def __init__(self, app):
        self.app = app

    def get_items(self):
        return ["item1", "item2"]

    def post_item(self, item_name: str):
        service = Service()
        db = Database()
        db.store(item_name)
        return {"message": "Item stored"}

router.get("/items", self.get_items)
router.post("/items", self.post_item)