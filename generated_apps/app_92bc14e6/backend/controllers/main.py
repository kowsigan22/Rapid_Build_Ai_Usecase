from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.get("/items")
def read_items():
    return [Item(name="Item 1", description="Description 1"), Item(name="Item 2", description="Description 2")]

@app.post("/items")
def create_item(item: Item):
    return item
