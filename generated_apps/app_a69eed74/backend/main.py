from fastapi import FastAPI
from backend.controllers import ItemController
app = FastAPI()
@app.get="/items")
def read_items():
    return [Item(name="item1", description="desc1"), Item(name="item2", description="desc2"])
@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item

if __name__ == "__main__":
    app.run()
