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
    "frontend/package.json": "{\\n  \\\"name\\\": \\\"fastapi-react-client\\\",\\n  \\\"version\\\": \\\"1.0.0\\\",\\n  \\\"private\\\": true,\\n  \\\"dependencies\\\": {\\n    \\\"react\\\": \\\"^18.0.0\\\",\\n    \\\"react-dom\\\": \\\"^18.0.0\\\",\\n    \\\"react-scripts\\\": \\\"5.0.0\\\",\\n    \\\"axios\\\": \\\"^1.6.0\\\"\\n  },\\n  \\\"scripts\\\": {\\n    \\\"start\\\": \\\"react-scripts start\\\",\\n    \\\"build\\\": \\\"react-scripts build\\\",\\n    \\\"test\\\": \\\"react-scripts test\\\",\\n    \\\"eject\\\": \\\"react-scripts eject\\\"\\n  }\\n}", 
    "frontend/src/index.js": "import React from \\\\\"react\\\\\";\\nimport ReactDOM from \\\\\"react-dom/client\\\\\";\\nimport App from \\\\\"./App\\\\\";\\n\\nconst root = ReactDOM.createRoot(document.getElementById(\\\"root\\\"));\\nroot.render(<App />);", 
    "frontend/src/App.js": "import React, { useState } from \\\\\"react\\\\\";\\nimport axios from \\\\\"axios\\\\\";\\nimport './App.css';\\n\\nfunction App() {\\n  const [name, setName] = useState(\\\"\\\");\\n  const [fatherName, setFatherName] = useState(\\\"\\\");\\n  const [address, setAddress] = useState(\\\"\\\");\\n  const [response, setResponse] = useState(null);\\n\\n  const handleSubmit = async (e) => {\\n    e.preventDefault();\\n    try {\\n      const res = await axios.get(\\`http://localhost:8000/submit?name=${name}&father_name=${fatherName}&address=${address}\\`);\\n      setResponse(res.data);\\n    } catch (err) {\\n      console.error(err);\\n    }\\n  };\\n\\n  return (\\n    <div className=\\\"container\\\">\\n      <h1 className=\\\"title\\\">FastAPI React Client</h1>\\n      <form onSubmit={handleSubmit} className=\\\"form\\\">\\n        <input type=\\\"text\\\" placeholder=\\\"Name\\\" value={name} onChange={(e) => setName(e.target.value)} />\\n        <input type=\\\"text\\\" placeholder=\\\"Father Name\\\" value={fatherName} onChange={(e) => setFatherName(e.target.value)} />\\n        <input type=\\\"text\\\" placeholder=\\\"Address\\\" value={address} onChange={(e) => setAddress(e.target.value)} />\\n        <button type=\\\"submit\\\">Submit</button>\\n      </form>\\n      {response && (\\n        <div className=\\\"response\\\">\\n          <h2>Response from Backend</h2>\\n          <p><strong>Name:</strong> {response.name}</p>\\n          <p><strong>Father Name:</strong> {response.father_name}</p>\\n          <p><strong>Address:</strong> {response.address}</p>\\n        </div>\\n      )}\\n    </div>\\n  );\\n}\\n\\nexport default App;", 
    "frontend/src/App.css": ".container {\\n  max-width: 600px;\\n  margin: 50px auto;\\n  padding: 20px;\\n  border: 1px solid #ccc;\\n  border-radius: 8px;\\n  background-color: #f9f9f9;\\n  box-shadow: 0 4px 8px rgba(0,0,0,0.1);\\n}\\n\\n.title {\\n  text-align: center;\\n  color: #333;\\n}\\n\\n.form {\\n  display: flex;\\n  flex-direction: column;\\n  gap: 10px;\\n}\\n\\n.form input {\\n  padding: 10px;\\n  border: 1px solid #ccc;\\n  border-radius: 4px;\\n}\\n\\n.form button {\\n  padding: 10px;\\n  background-color: #007bff;\\n  color: white;\\n  border: none;\\n  border-radius: 4px;\\n  cursor: pointer;\\n}\\n\\n.form button:hover {\\n  background-color: #0056b3;\\n}\\n\\n.response {\\n  margin-top: 20px;\\n  padding: 15px;\\n  border: 1px solid #007bff;\\n  border-radius: 4px;\\n  background-color: #e9f5ff;\\n}\\n.response h2 {\\n  margin-bottom: 10px;\\n}\\n.response p {\\n  margin: 5px 0;\\n}" 
  }, 
  "execution_descriptor": { 
    "language": "javascript", 
    "framework": "react", 
    "application_type": "frontend", 
    "working_dir": "frontend", 
    "build": "npm run build", 
    "run": "npm start", 
    "long_running": true, 
    "ports": [3000], 
    "healthcheck": null 
  } 
}

"""