from fastapi import FastAPI
app = FastAPI()
@app.get("/items")
def read_items():
    return [{"id": i, "name": f"Item {i}"} for i in range(10)]
@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item
items = []
if __name__ == "__main__":
    from fastapi uvicorn.run(app, host="0.0.0.0", port=8000)