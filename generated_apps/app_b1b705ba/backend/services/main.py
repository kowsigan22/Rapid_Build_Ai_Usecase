from backend.db.main import InMemoryDatabase
from fastapi.responses import JSONResponse
class Service:
    def __init__(self):
        self.db = InMemoryDatabase()
    def read_items(self) -> JSONResponse:
        return JSONResponse(content=self.db.get_items(), media_type="application/json")
    def create_item(self, item: dict) -> JSONResponse:
        return JSONResponse(content=self.db.create_item(item), media_type="application/json")
