from fastapi import FastAPI
from backend.services.service import Service
app = FastAPI()
@app.get("/items")
def read_items():
    return [Service().get_all_items()]
@app.post("/items")
def create_item(item: dict):
    service = Service()
    item_id = service.create_item(item)
    return {"item_id": item_id}

if __name__ == "__main__":
    from uvicorn.main import run
    run("backend.main:app", host="0.0.0.0", port=8000, debug=True)
