from typing import List
class DB:
    items = []
    def get_all_items(self):
        return self.items
    def create_item(self, item: dict):
        self.items.append(item)
