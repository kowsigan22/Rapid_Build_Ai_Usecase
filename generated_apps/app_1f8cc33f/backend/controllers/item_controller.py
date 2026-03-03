from fastapi import APIRouter
from backend.services import ItemService
router = APIRouter()
@router.get("/items")
def read_items():
    return [Item(name="sample", price=10)]
@router.post("/items")
def create_item(item: dict):
    items.append(item)
    return item
