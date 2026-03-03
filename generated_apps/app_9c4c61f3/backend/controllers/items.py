from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel
class Item(BaseModel):
    name: str
    price: int
class ItemsController:
    def __init__(self):
        self.items = []
    def get(self):
        return JSONResponse(content={'items': self.items}, media_type='application/json')
    def post(self, item: Item):
        self.items.append(item)
        return JSONResponse(content={'item': item}, media_type='application/json')
