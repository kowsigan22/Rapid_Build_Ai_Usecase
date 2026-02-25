from fastapi import APIRouter
from backend.services import Service
router = APIRouter()
@router.get("/items")
def read_items():
    return [Service().read_items()]
