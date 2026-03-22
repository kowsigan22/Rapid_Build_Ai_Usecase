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
    "backend/__init__.py": "", 
    "backend/main.py": "from fastapi import FastAPI\\nfrom fastapi.middleware.cors import CORSMiddleware\\n\\napp = FastAPI()\\n\\napp.add_middleware(\\n    CORSMiddleware,\\n    allow_origins=[\\"*\\"],\\n    allow_credentials=True,\\n    allow_methods=[\\"*\\"],\\n    allow_headers=[\\"*\\"],\\n)\\n\\n@app.get(\\"/submit\\")\\ndef submit(name: str, father_name: str, address: str):\\n    return {\\n        \\"name\\": name,\\n        \\"father_name\\": father_name,\\n        \\"address\\": address\\n    }\\n", 
    "backend/requirements.txt": "fastapi\\nuvicorn\\n" 
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
          "path": "/submit?name=John&father_name=Doe&address=NY", 
          "method": "GET", 
          "expected_status": 200 
        } 
      ] 
    } 
  } 
}

"""