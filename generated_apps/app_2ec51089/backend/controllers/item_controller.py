from fastapi import Response, Request
from backend.services import Service
class ItemController:
    async def read_items(self):
        return [Service.get_all_items()]
    async def create_item(self, item: dict):
        Service.create_item(item)
        return Response(status_code=201)