from typing import List, Dict
class InMemoryDB:
    def __init__(self):
        self.items = []
    def get_items(self) -> List[Dict]:
        return self.items
    def add_item(self, item: Dict) -> Dict:
        self.items.append(item)
        return item
