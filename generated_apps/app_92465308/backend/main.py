from fastapi import FastAPI
from backend.controllers import items_controller
app = FastAPI()
@app.get("/items")
def read_items():
    return items_controller.read_items()
@app.post("/items")
def create_item(item: dict):
    return items_controller.create_item(item)
