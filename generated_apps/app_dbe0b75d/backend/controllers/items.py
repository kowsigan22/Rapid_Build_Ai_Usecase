from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    price: int
class ItemsController:
    def __init__(self):
        self.items = {}
    async def get_items(self, request):
        return JSONResponse(content={'items': list(self.items.values())}, media_type='application/json')
    async def post_item(self, request):
        item = Item(**request.json()).dict()
        self.items[item['name']] = item
        return JSONResponse(content=item, media_type='application/json')
