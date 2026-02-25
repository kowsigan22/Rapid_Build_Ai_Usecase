from fastapi import FastAPI
from backend.controllers import ItemController
app = FastAPI()
@app.get="/items")
def read_items():
    return [Item(name="item1", description="desc1"), Item(name="item2", description="desc2")]
@app.post="/items")
def create_item(item: dict):
    items.append(Item(**item))
if __name__ == "__main__":
    from backend.services import Service
    from backend.db import DB, Item
    service = Service(DB())
    app.include_router(ItemController(service).router)
    uvicorn.run(app, host="0.0.0.0", port=8000)