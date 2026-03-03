from fastapi import FastAPI
app = FastAPI()
from .controllers import item_controller
@app.get("/items")
def read_items():
    return item_controller.read_items()
@app.post("/items")
def create_item(item: dict):
    return item_controller.create_item(item)
