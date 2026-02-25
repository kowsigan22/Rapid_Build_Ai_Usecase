from fastapi import FastAPI
from backend.controllers import ItemController
app = FastAPI()
@app.get("/items")
def read_items():
    return [Item(name="Item 1"), Item(name="Item 2")]
class Item:
    def __init__(self, name):
        self.name = name

from backend.services import Service
from backend.db import DB
class ItemController(Service):
    def read_items(self):
        return [DB().get_item(name) for name in ["Item 1", "Item 2"]]

from backend.db import InMemoryDatabase
class DB:
    def __init__(self):
        self.items = {}
    def get_item(self, name):
        return self.items.get(name)

from backend.services import Service
class Service:
    def read_items(self):
        return [DB().get_item(name) for name in ["Item 1", "Item 2"]]

from backend.controllers import ItemController
app = FastAPI()
@app.post("/items")
def create_item(item: dict):
    DB().set_item(**item)
    return item
