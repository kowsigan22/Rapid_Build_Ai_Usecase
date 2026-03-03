from typing import List, Dict
class InMemoryDB:
    items: List[Dict] = []
    def get_all_items(self):
        return self.items
    def add_item(self, item: dict):
        self.items.append(item)
