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
  "generated_files": {
    "backend/__init__.py": "",
    "backend/main.py": "from fastapi import FastAPI\\nfrom backend.controllers import ItemController\\nfrom backend.services import Service\\napp = FastAPI()\\ncontroller = ItemController(app)\\napp.include_router(controller.router)\\n",
    "backend/controllers/__init__.py": "",
    "backend/controllers/item_controller.py": "from fastapi import APIRouter\\nfrom backend.services.item_service import ItemService\\nrouter = APIRouter()\\nservice = ItemService()\\n@router.get(\\"/items\\")\\ndef get_items():\\n    return service.get_items()\\n@router.post(\\"/items\\")\\ndef create_item(item: dict):\\n    return service.add_item(item)",
    "backend/services/__init__.py": "",
    "backend/services/item_service.py": "from backend.db.in_memory_db import InMemoryDB\\nclass ItemService:\\n    def __init__(self):\\n        self.db = InMemoryDB()\\n    def get_items(self):\\n        return self.db.get_items()\\n    def add_item(self, item):\\n        self.db.add_item(item)\\n        return item",
    "backend/db/__init__.py": "",
    "backend/db/in_memory_db.py": "class InMemoryDB:\\n    def __init__(self):\\n        self.items = []\\n    def get_items(self):\\n        return self.items\\n    def add_item(self, item):\\n        self.items.append(item)",
    "backend/requirements.txt": "fastapi\\nuvicorn\\nrequests"
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