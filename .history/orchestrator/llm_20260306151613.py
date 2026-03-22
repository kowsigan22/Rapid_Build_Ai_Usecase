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
"backend/main.py": "from fastapi import FastAPI\nfrom backend.controllers.item_controller import router as item_router\n\napp = FastAPI(title="Sample FastAPI Layered Service")\n\napp.include_router(item_router)\n\n@app.get
("/health")\ndef health():\n return {"status": "ok"}\n",
"backend/controllers/item_controller.py": "from fastapi import APIRouter\nfrom pydantic import BaseModel\nfrom backend.services.item_service import ItemService\n\nrouter = APIRouter(prefix="/items", tags=["items"])\n\nservice = ItemService()\n\nclass ItemRequest(BaseModel):\n name: str\n description: str\n\n@router.get
("/")\ndef get_items():\n return service.get_items()\n\n@router.post
("/")\ndef create_item(item: ItemRequest):\n return service.create_item(item.dict())\n",
"backend/services/item_service.py": "from backend.db.inmemory_db import InMemoryDB\n\nclass ItemService:\n\n def init(self):\n self.db = InMemoryDB()\n\n def get_items(self):\n return self.db.get_all()\n\n def create_item(self, item):\n return self.db.insert(item)\n",
"backend/db/inmemory_db.py": "class InMemoryDB:\n\n _items = []\n\n def get_all(self):\n return self._items\n\n def insert(self, item):\n item_id = len(self._items) + 1\n record = {"id": item_id, **item}\n self._items.append(record)\n return record\n",
"backend/requirements.txt": "fastapi\nuvicorn\npydantic\n"
},
"execution_descriptor": {
"language": "python",
"framework": "FastAPI",
"application_type": "web-service",
"working_dir": "backend",
"build": null,
"run": "uvicorn backend.main:app --host 0.0.0.0 --port 8000",
"long_running": true,
"ports": [8000],
"healthcheck": {
"base_url": "http://localhost:8000
",
"endpoints": [
{
"path": "/health",
"method": "GET",
"expected_status": 200
}
]
}
}
}"""