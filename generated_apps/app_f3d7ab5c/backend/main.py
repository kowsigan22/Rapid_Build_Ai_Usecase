from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int

@app.post("/items")
def create_item(item: Item):
    print(f"Created item {item.name} at ${item.price}")

if __name__ == "__main__":
    from backend.services.db import DB
    from backend.controllers.items import ItemsController
    app.include_router(ItemsController.router)
    uvicorn.run(app, host="0.0.0.0", port=8000)