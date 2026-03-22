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
    return """{
"generated_files": {
"backend/init.py": "",
"backend/main.py": "from fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\nfrom backend.controllers.input_controller import router as input_router\n\napp = FastAPI()\n\napp.add_middleware(\n CORSMiddleware,\n allow_origins=[""],\n allow_credentials=True,\n allow_methods=[""],\n allow_headers=["*"],\n)\n\napp.include_router(input_router)\n\n@app.get
("/")\ndef root():\n return {"status": "running"}\n",
"backend/controllers/init.py": "",
"backend/controllers/input_controller.py": "from fastapi import APIRouter\nfrom backend.models.input_model import UserInput\nfrom backend.services.input_service import InputService\n\nrouter = APIRouter()\nservice = InputService()\n\n@router.get
("/inputs")\ndef get_inputs():\n return service.get_all_inputs()\n\n@router.post
("/inputs")\ndef add_input(user_input: UserInput):\n return service.add_input(user_input.dict())\n",
"backend/services/init.py": "",
"backend/services/input_service.py": "from backend.db.in_memory_db import db_instance\n\nclass InputService:\n\n def get_all_inputs(self):\n return db_instance.get_all()\n\n def add_input(self, input_data):\n return db_instance.add(input_data)\n",
"backend/db/init.py": "",
"backend/db/in_memory_db.py": "class InMemoryDB:\n\n def init(self):\n self.inputs = []\n\n def get_all(self):\n return self.inputs\n\n def add(self, input_data):\n self.inputs.append(input_data)\n return input_data\n\n\ndb_instance = InMemoryDB()\n",
"backend/models/init.py": "",
"backend/models/input_model.py": "from pydantic import BaseModel\n\nclass UserInput(BaseModel):\n text: str\n",
"backend/requirements.txt": "fastapi\nuvicorn\npydantic\n"
},
"execution_descriptor": {
"language": "python",
"framework": "fastapi",
"application_type": "web-service",
"working_dir": "backend",
"build": null,
"run": "uvicorn backend.main:app --host 0.0.0.0 --port 8000",
"long_running": true,
"ports": [
8000
],
"healthcheck": {
"base_url": "http://localhost:8000
",
"endpoints": [
{
"path": "/",
"method": "GET",
"expected_status": 200
},
{
"path": "/inputs",
"method": "GET",
"expected_status": 200
},
{
"path": "/inputs",
"method": "POST",
"expected_status": 200,
"payload": {
"text": "example input"
}
}
]
}
}
}"""