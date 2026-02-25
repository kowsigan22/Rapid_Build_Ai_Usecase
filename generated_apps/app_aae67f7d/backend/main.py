from fastapi import FastAPI
from backend.controllers import item_controller
from backend.services import service_layer
from backend.db import db_layer
app = FastAPI()
@app.get("/items")
def read_items():
    return item_controller.read_items()
@app.post("/items")
def create_item(item: dict):
    return item_controller.create_item(item)
