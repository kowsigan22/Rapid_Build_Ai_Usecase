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
    "frontend/package.json": "{\\\"name\\\": \\\"frontend\\\", \\\"version\\\": \\\"1.0.0\\\", \\\"private\\\": true, \\\"dependencies\\\": {\\\"react\\\": \\\"^18.0.0\\\", \\\"react-dom\\\": \\\"^18.0.0\\\", \\\"axios\\\": \\\"^1.6.0\\\", \\\"vite\\\": \\\"^5.0.0\\\"}, \\\"scripts\\\": {\\\"start\\\": \\\"vite\\\", \\\"build\\\": \\\"vite build\\\"}}",
    "frontend/index.html": "<!DOCTYPE html>\\n<html lang=\\\"en\\\">\\n<head>\\n  <meta charset=\\\"UTF-8\\\" />\\n  <meta name=\\\"viewport\\\" content=\\\"width=device-width, initial-scale=1.0\\\" />\\n  <title>React FastAPI Client</title>\\n</head>\\n<body>\\n  <div id=\\\"root\\\"></div>\\n  <script type=\\\"module\\\" src=\\\"/src/main.jsx\\\"></script>\\n</body>\\n</html>",
    "frontend/src/main.jsx": "import React from \\\"react\\\";\\nimport ReactDOM from \\\"react-dom/client\\\";\\nimport App from \\\"./App\\\";\\n\\nReactDOM.createRoot(document.getElementById(\\\"root\\\")).render(<App />);",
    "frontend/src/App.jsx": "import React, { useState } from \\\"react\\\";\\nimport axios from \\\"axios\\\";\\n\\nfunction App() {\\n  const [name, setName] = useState(\\\"\\\");\\n  const [fatherName, setFatherName] = useState(\\\"\\\");\\n  const [address, setAddress] = useState(\\\"\\\");\\n  const [response, setResponse] = useState(null);\\n\\n  const handleSubmit = async (e) => {\\n    e.preventDefault();\\n    try {\\n      const res = await axios.post(\\\"http://localhost:8000/user\\\", {\\n        name,\\n        father_name: fatherName,\\n        address\\n      });\\n      setResponse(res.data);\\n    } catch (err) {\\n      console.error(err);\\n    }\\n  };\\n\\n  const checkStatus = async () => {\\n    try {\\n      const res = await axios.get(\\\"http://localhost:8000/\\\");\\n      setResponse(res.data);\\n    } catch (err) {\\n      console.error(err);\\n    }\\n  };\\n\\n  return (\\n    <div style={{ padding: \\\"20px\\\" }}>\\n      <h1>FastAPI React Client</h1>\\n      <form onSubmit={handleSubmit}>\\n        <div>\\n          <label>Name: </label>\\n          <input value={name} onChange={(e) => setName(e.target.value)} />\\n        </div>\\n        <div>\\n          <label>Father Name: </label>\\n          <input value={fatherName} onChange={(e) => setFatherName(e.target.value)} />\\n        </div>\\n        <div>\\n          <label>Address: </label>\\n          <input value={address} onChange={(e) => setAddress(e.target.value)} />\\n        </div>\\n        <button type=\\\"submit\\\">Submit</button>\\n      </form>\\n      <button onClick={checkStatus}>Check API Status</button>\\n      {response && (<pre>{JSON.stringify(response, null, 2)}</pre>)}\\n    </div>\\n  );\\n}\\n\\nexport default App;"
  },
  "execution_descriptor": {
    "language": "javascript",
    "framework": "react",
    "application_type": "frontend",
    "working_dir": "frontend",
    "build": "npm run build",
    "run": "npm start",
    "long_running": true,
    "ports": [5173],
    "healthcheck": null
  }
}
"""