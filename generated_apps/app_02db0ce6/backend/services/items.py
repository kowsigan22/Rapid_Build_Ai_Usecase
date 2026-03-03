from backend.db.database import Database
class ItemsService:
  def __init__(self, db: Database):
    self.db = db
  def get(self):
    return self.db.get_all()
  def post(self, item: dict):
    self.db.save(item)
