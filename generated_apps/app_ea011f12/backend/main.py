from fastapi import FastAPI
from backend.controllers.main import app
from backend.services.main import ItemService
app = FastAPI()
item_service = ItemService(InMemoryDatabase())
@app.get("/items")
def read_items():
    return item_service.get_items()
@app.post("/items")
def create_item(item: dict):
    return item_service.create_item(item)
