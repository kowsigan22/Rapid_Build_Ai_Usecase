from typing import List
class ItemDatabase:
    def __init__(self):
        self.items = []
    def get_all_items(self):
        return self.items
    def save_item(self, item: dict):
        self.items.append(item)
