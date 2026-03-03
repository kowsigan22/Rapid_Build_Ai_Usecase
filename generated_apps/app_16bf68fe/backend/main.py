from fastapi import FastAPI
from backend.controllers.items import ItemsController
app = FastAPI()
@app.get("/items")
def read_items():
    return ItemsController().get_all_items()
@app.post("/items")
def create_item(item: dict):
    return ItemsController().create_item(item)
