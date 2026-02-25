from typing import List, Dict
class Database:
    def __init__(self):
        self.items: List[Dict] = []
    def get_all_items(self):
        return self.items
    def create_item(self, item: Dict):
        self.items.append(item)
        return item