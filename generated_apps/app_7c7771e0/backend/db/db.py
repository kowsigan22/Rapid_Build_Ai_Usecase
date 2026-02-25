from typing import List
class Database:
    def __init__(self):
        self.items = []
    def get_items(self) -> List[dict]:
        return [item.__dict__ for item in self.items]
    def create_item(self, request: dict) -> dict:
        self.items.append(request)
        return request