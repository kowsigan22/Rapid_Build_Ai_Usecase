from typing import List
class Database:
    def __init__(self):
        self.items = []
    def get_items(self):
        return self.items
    def store_item(self, item: Item):
        self.items.append(item)
