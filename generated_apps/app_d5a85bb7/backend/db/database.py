from typing import List
class Database:
    def __init__(self):
        self.items: List[dict] = []
    def get_items(self):
        return self.items.copy()
    def store_item(self, item: dict):
        self.items.append(item)
