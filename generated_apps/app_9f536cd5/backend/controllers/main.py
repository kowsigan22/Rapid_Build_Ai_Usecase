from fastapi import FastAPI
from pydantic import BaseModel
from backend.services.service import Service
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.get("/items")
def read_items():
    return [Item(name="item1", description="desc1"), Item(name="item2", description="desc2")]

@app.post("/items")
def create_item(item: Item):
    return item
