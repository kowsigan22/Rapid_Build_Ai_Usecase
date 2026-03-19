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
    return """{ "generated_files": { "backend/init.py": "", "backend/main.py": "from fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom backend.controllers.user_controller import router as user_router\n\napp = FastAPI()\n\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=[\"\"],\n    allow_credentials=True,\n    allow_methods=[\"\"],\n    allow_headers=[\"*\"],\n)\n\napp.include_router(user_router)\n\n@app.get(\"/\")\ndef root():\n    return {\"status\": \"running\"}\n", "backend/controllers/init.py": "", "backend/controllers/user_controller.py": "from fastapi import APIRouter\nfrom backend.models.user import User\n\nrouter = APIRouter()\n\n@router.post(\"/user\")\ndef create_user(user: User):\n    return {\n        \"name\": user.name,\n        \"father_name\": user.father_name,\n        \"address\": user.address\n    }\n", "backend/models/init.py": "", "backend/models/user.py": "from pydantic import BaseModel\n\nclass User(BaseModel):\n    name: str\n    father_name: str\n    address: str\n", "backend/requirements.txt": "fastapi\nuvicorn\npydantic\nrequests" }, "execution_descriptor": { "language": "python", "framework": "fastapi", "application_type": "web-service", "working_dir": "backend", "build": null, "run": "uvicorn backend.main:app --host 0.0.0.0 --port 8000", "long_running": true, "ports": [8000], "healthcheck": { "base_url": "http://localhost:8000", "endpoints": [ { "path": "/", "method": "GET", "expected_status": 200 }, { "path": "/user", "method": "POST", "expected_status": 200, "payload": { "name": "John Doe", "father_name": "Richard Roe", "address": "123 Main Street" } } ] } } }
"""