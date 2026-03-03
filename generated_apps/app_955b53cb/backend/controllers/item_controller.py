from backend.models import Item
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/items')
def get_items():
    return [Item(name='Item 1', price=10), Item(name='Item 2', price=20)]