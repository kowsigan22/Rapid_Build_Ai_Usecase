from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int

@app.post('/items')
def create_item(item: Item):
    print(f'Created item {item.name} at ${item.price}')