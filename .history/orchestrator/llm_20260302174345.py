from openai import OpenAI
from dotenv import load_dotenv

# Load env (still useful later)
load_dotenv()

# Ollama exposes an OpenAI-compatible API
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # dummy key, required by SDK
)

def call_llm(prompt: str) -> str:
    # response = client.chat.completions.create(
    #     model="llama3",
    #     messages=[
    #         {"role": "user", "content": prompt}
    #     ],
    #     temperature=0.2
    # )

    # return response.choices[0].message.content
    return """
{
  "backend/main.py": """
from fastapi import FastAPI
from controllers.item_controller import router as item_router

app = FastAPI()

app.include_router(item_router)

@app.get("/")
def root():
    return {"status": "running"}
""",

"backend/requirements.txt": """
fastapi
uvicorn
pydantic
""",

"backend/models/item.py": """
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: int
""",

"backend/db/in_memory_db.py": """
class InMemoryDB:
    def __init__(self):
        self.items = []

    def get_all(self):
        return self.items

    def add(self, item):
        self.items.append(item)
        return item

db_instance = InMemoryDB()
""",

"backend/services/item_service.py": """
from db.in_memory_db import db_instance

class ItemService:

    def get_items(self):
        return db_instance.get_all()

    def create_item(self, item):
        return db_instance.add(item)
""",

"backend/controllers/item_controller.py": """
from fastapi import APIRouter
from models.item import Item
from services.item_service import ItemService

router = APIRouter()
service = ItemService()

@router.get("/items")
def get_items():
    return service.get_items()

@router.post("/items")
def create_item(item: Item):
    return service.create_item(item.dict())
"""
},
  "execution_descriptor": {
    "language": "python",
    "framework": "fastapi",
    "application_type": "web-service",
    "working_dir": "backend",
    "build": null,
    "run": "uvicorn main:app --host 0.0.0.0 --port 8000",
    "long_running": true,
    "ports": [8000],
    "healthcheck": {
      "base_url": "http://localhost:8000",
      "endpoints": [
        {
          "path": "/items",
          "method": "GET",
          "expected_status": 200
        },
        {
          "path": "/items",
          "method": "POST",
          "expected_status": 200,
          "payload": {
            "name": "apple",
            "price": 10
          }
        }
      ]
    }
  }
}
"""