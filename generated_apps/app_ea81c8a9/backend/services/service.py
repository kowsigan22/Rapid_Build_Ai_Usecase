from backend.db.database import database
from fastapi.responses import JSONResponse
class Service:
    def __init__(self): pass
    def get_items(self):
        return JSONResponse(content=database.get_items(), media_type="application/json")
    def create_item(self, item: dict):
        database.add_item(item)
