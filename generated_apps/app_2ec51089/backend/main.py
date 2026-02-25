from fastapi import FastAPI
from backend.controllers import ItemController
from backend.services import Service
from backend.db import DB
app = FastAPI()
@app.get('/items')
def read_items():
    return [DB.items]
@app.post('/items')
async def create_item(item: dict):
    DB.items.append(item)
    return item
