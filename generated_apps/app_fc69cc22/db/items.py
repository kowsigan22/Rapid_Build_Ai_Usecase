from typing import List
items: List[dict] = []
def get_items() -> List[dict]:
    return items
def post_item(item: dict):
    global items
    items.append(item)
