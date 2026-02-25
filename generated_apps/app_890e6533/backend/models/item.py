from typing import Dict
class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    def to_dict(self) -> Dict:
        return {'name': self.name, 'description': self.description}
