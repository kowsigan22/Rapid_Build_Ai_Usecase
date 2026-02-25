from fastapi import APIRouter
from backend.services import ItemService
router = APIRouter()
@router.get("/items")
def read_items():
    return [Item(name="item1", description="desc1"), Item(name="item2", description="desc2")]