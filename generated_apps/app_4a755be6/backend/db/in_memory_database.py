from typing import List, Dict
class InMemoryDatabase:
    items: List[Dict]
    def __init__(self):
        self.items = []
    def get_items(self):
        return self.items