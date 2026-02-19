from backend.db.items import Items
class ItemService:
    def __init__(self):
        self.items = Items()
    def get_items(self) -> List[Dict]:
        return self.items.get_items()
    def create_item(self, item: Dict) -> Dict:
        return self.items.create_item(item)