from typing import List
class ItemService:
    def get_items(self) -> List[dict]:
        with open('db/items.json', 'r') as f:
            return [json.load(f)]
    def post_item(self, item: dict):
        with open('db/items.json', 'a') as f:
            json.dump(item, f)
