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
    response = client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
    return """{
  "generated_files": {
    "backend/__init__.py": "",
    "backend/main.py": "from fastapi import FastAPI\\nfrom fastapi.middleware.cors import CORSMiddleware\\nfrom backend.controllers.item_controller import router as item_router\\n\\napp = FastAPI()\\n\\napp.add_middleware(\\n    CORSMiddleware,\\n    allow_origins=[\\"*\\"],\\n    allow_credentials=True,\\n    allow_methods=[\\"*\\"],\\n    allow_headers=[\\"*\\"],\\n)\\n\\napp.include_router(item_router)\\n\\n@app.get(\\"/\\")\\ndef root():\\n    return {\\"status\\": \\"running\\"}\\n",
    "backend/controllers/__init__.py": "",
    "backend/controllers/item_controller.py": "from fastapi import APIRouter\\nfrom backend.models.item import Item\\nfrom backend.services.item_service import ItemService\\n\\nrouter = APIRouter()\\nservice = ItemService()\\n\\n@router.get(\\"/items\\")\\ndef get_items():\\n    return service.get_items()\\n\\n@router.post(\\"/items\\")\\ndef create_item(item: Item):\\n    return service.create_item(item.dict())\\n",
    "backend/services/__init__.py": "",
    "backend/services/item_service.py": "from backend.db.in_memory_db import db_instance\\n\\nclass ItemService:\\n\\n    def get_items(self):\\n        return db_instance.get_all()\\n\\n    def create_item(self, item):\\n        return db_instance.add(item)\\n",
    "backend/db/__init__.py": "",
    "backend/db/in_memory_db.py": "class InMemoryDB:\\n    def __init__(self):\\n        self.items = []\\n\\n    def get_all(self):\\n        return self.items\\n\\n    def add(self, item):\\n        self.items.append(item)\\n        return item\\n\\n\\ndb_instance = InMemoryDB()\\n",
    "backend/models/__init__.py": "",
    "backend/models/item.py": "from pydantic import BaseModel\\n\\nclass Item(BaseModel):\\n    name: str\\n    price: int\\n",
    "backend/requirements.txt": "fastapi\\nuvicorn\\npydantic\\nrequests"
  },
  "execution_descriptor": {
    "language": "python",
    "framework": "fastapi",
    "application_type": "web-service",
    "working_dir": "backend",
    "build": null,
    "run": "uvicorn backend.main:app --host 0.0.0.0 --port 8000",
    "long_running": true,
    "ports": [8000],
    "healthcheck": {
      "base_url": "http://localhost:8000",
      "endpoints": [
        {
          "path": "/",
          "method": "GET",
          "expected_status": 200
        },
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
}"""