from typing import List
class Database:
    def __init__(self):
        self.items = {}
    async def get_all_items(self):
        return list(self.items.values())
    async def save_item(self, item):
        self.items[item['name']] = item
