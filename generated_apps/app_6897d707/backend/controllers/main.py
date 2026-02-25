from fastapi import FastAPI, Response
app = FastAPI()

@app.post("/items")
def create_item(item: Item):
    return item