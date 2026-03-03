from fastapi.responses import JSONResponse
from typing import List
class ItemsController:
    def __init__(self):
        self.items: List[dict] = []
    def get(self):
        return JSONResponse(content={'items': self.items}, media_type='application/json')
    def post(self, item: dict):
        self.items.append(item)
        return JSONResponse(content=item, media_type='application/json')
