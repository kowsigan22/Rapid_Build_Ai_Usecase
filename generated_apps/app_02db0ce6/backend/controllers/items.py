from fastapi.responses import JSONResponse
from typing import List
class ItemsController:
  def __init__(self):
    self.db = {}
  def get(self):
    return JSONResponse(content={'items': list(self.db.keys())}, media_type='application/json')
  def post(self, item: dict):
    self.db[item['name']] = item
    return JSONResponse(content=item, media_type='application/json')
