from backend.db.database import Database
class ItemsService:
    def __init__(self):
        self.db = Database()
    async def get_items(self):
        return self.db.get_all_items()
    async def post_item(self, item):
        await self.db.save_item(item)
