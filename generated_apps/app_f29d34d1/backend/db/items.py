from typing import List, Dict
class Items:
    def __init__(self):
        self.items = {}
    def get_items(self) -> List[Dict]:
        return list(self.items.values())
    def create_item(self, item: Dict):
        self.items[len(self.items)] = item
        return item