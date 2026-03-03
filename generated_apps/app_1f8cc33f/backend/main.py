from fastapi import FastAPI
from backend.controllers import ItemController
app = FastAPI()
@app.get("/items")
def read_items():
    return [Item(name="sample", price=10)]
@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item
