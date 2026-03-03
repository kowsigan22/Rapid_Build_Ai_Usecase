from fastapi.responses import JSONResponse
from typing import List
from backend.services.items import ItemsService
class ItemsController:
    def __init__(self):
        self.service = ItemsService()
    def get(self):
        return JSONResponse(content=self.service.get_items(), media_type='application/json')
    def post(self, item: dict):
        self.service.create_item(item)
        return JSONResponse(content=item, media_type='application/json')
