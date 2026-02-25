from fastapi import FastAPI
from backend.controllers import ItemController
app = FastAPI()
@app.get("/items")
def read_items():
    return [Item(name="Item 1", description="Description 1"), Item(name="Item 2", description="Description 2"]
@app.post("/items")
def create_item(item: dict):
    items = [Item(name=item["name"], description=item["description"])]
    return items

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

from backend.services import Service
from backend.db import DB
