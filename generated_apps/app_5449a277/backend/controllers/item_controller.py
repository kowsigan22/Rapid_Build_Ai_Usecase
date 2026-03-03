from fastapi.responses import JSONResponse
from .models import Item
class ItemController:
    def read_items(self):
        return [Item(name="item1", price=10), Item(name="item2", price=20)]
    def create_item(self, item: dict):
        return JSONResponse(content=item, media_type="application/json")
