from backend.db.in_memory_db import InMemoryDB
from fastapi.responses import JSONResponse
from fastapi.requests import Request
class Service:
    def __init__(self):
        self.db = InMemoryDB()

    def get_items(self, request: Request):
        return JSONResponse(content=self.db.get_items(), media_type="application/json")

    def create_item(self, item: dict):
        self.db.add_item(item)
        return JSONResponse(content=item, media_type="application/json")