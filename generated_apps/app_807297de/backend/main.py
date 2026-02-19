from fastapi import FastAPI
from backend.controllers.main import app as controllers_app
from backend.services.main import app as services_app
app = FastAPI()
@app.on_event("startup")
def startup():
    controllers_app.mount("/items", read_items, create_item)
    services_app.mount("/items", read_items, create_item)
