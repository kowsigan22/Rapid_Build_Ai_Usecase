from typing import List, Dict
items: List[Dict] = []
def get_items():
    return items
def add_item(item: Dict):
    items.append(item)
