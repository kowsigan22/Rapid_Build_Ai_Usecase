from backend.services import item_service
from fastapi.responses import JSONResponse
class ItemsController:
    def read_items(self):
        return JSONResponse(content=item_service.read_items(), media_type="application/json")
    def create_item(self, item: dict):
        return JSONResponse(content=item_service.create_item(item), media_type="application/json")
