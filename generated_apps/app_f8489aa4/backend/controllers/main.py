from fastapi import FastAPI
from backend.services.service import Service
app = FastAPI()
@app.get("/items")
def read_items():
    return [item for item in items]
@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item
if __name__ == "__main__":
    from backend.services.service import Service
    service = Service()
    app.include_router(service.router)
    uvicorn.run(app, host="0.0.0.0", port=8000)
