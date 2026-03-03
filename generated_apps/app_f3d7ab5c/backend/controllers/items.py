from fastapi.responses import JSONResponse
from backend.models.item import Item

class ItemsController:
    def __init__(self):
        self.db = DB()

    def get(self):
        items = [Item(name="item1", price=10), Item(name="item2", price=20)]
        return JSONResponse(content={'items': items}, media_type='application/json')

    router = FastAPI().include_router(get)
