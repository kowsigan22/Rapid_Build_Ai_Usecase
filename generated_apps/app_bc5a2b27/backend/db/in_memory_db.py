from typing import List
class InMemoryDB:
    def __init__(self):
        self.items = [{'name': 'Item 1', 'description': 'Description 1'}, {'name': 'Item 2', 'description': 'Description 2'}]
    def get_all_items(self) -> List[dict]:
        return self.items