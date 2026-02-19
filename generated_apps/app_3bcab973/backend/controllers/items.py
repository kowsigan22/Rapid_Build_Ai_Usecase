from fastapi import APIRouter
from backend.controllers.main import app
router = APIRouter()
@router.get("/items")
def read_items():
    return app.read_items()