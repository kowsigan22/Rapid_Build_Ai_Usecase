from fastapi import APIRouter
from .models import Item
router = APIRouter()
@router.get("/items")
def read_items():
    return [Item(name="Item1"), Item(name="Item2"]]
@router.post("/items")
def create_item(item: dict):
    print(item)
