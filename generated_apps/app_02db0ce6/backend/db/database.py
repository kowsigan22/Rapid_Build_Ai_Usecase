from typing import Dict
class Database:
  def __init__(self):
    self.data = {}
  def get_all(self):
    return list(self.data.keys())
  def save(self, item: dict):
    self.data[item['name']] = item
