from typing import Dict
class InMemoryDatabase:
    def __init__(self):
        self.items: Dict[str, dict] = {}
    def set_item(self, **kwargs):
        self.items.update(kwargs)
    def get_item(self, name):
        return self.items.get(name)
