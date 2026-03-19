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
    "frontend/package.json": "{\\n  \\\"name\\\": \\\"frontend\\\",\\n  \\\"version\\\": \\\"1.0.0\\\",\\n  \\\"private\\\": true,\\n  \\\"dependencies\\\": {\\n    \\\"react\\\": \\\"^18.0.0\\\",\\n    \\\"react-dom\\\": \\\"^18.0.0\\\",\\n    \\\"react-scripts\\\": \\\"5.0.0\\\",\\n    \\\"axios\\\": \\\"^1.6.0\\\"\\n  },\\n  \\\"scripts\\\": {\\n    \\\"start\\\": \\\"react-scripts start\\\",\\n    \\\"build\\\": \\\"react-scripts build\\\"\\n  }\\n}",
    "frontend/public/index.html": "<!DOCTYPE html>\\n<html lang=\\\"en\\\">\\n  <head>\\n    <meta charset=\\\"utf-8\\\" />\\n    <meta name=\\\"viewport\\\" content=\\\"width=device-width, initial-scale=1\\\" />\\n    <title>React App</title>\\n  </head>\\n  <body>\\n    <div id=\\\"root\\\"></div>\\n  </body>\\n</html>\\n",
    "frontend/src/index.js": "import React from 'react';\\nimport ReactDOM from 'react-dom/client';\\nimport App from './App';\\n\\nconst root = ReactDOM.createRoot(document.getElementById('root'));\\nroot.render(<App />);\\n",
    "frontend/src/App.js": "import React, { useState, useEffect } from 'react';\\nimport axios from 'axios';\\n\\nfunction App() {\\n  const [inputs, setInputs] = useState([]);\\n  const [name, setName] = useState('');\\n  const [message, setMessage] = useState('');\\n\\n  useEffect(() => {\\n    axios.get('http://localhost:8000/inputs')\\n      .then(res => setInputs(res.data))\\n      .catch(err => console.error(err));\\n  }, []);\\n\\n  const handleSubmit = (e) => {\\n    e.preventDefault();\\n    axios.post('http://localhost:8000/input', { name, message })\\n      .then(res => {\\n        setInputs(prev => [...prev, res.data]);\\n        setName('');\\n        setMessage('');\\n      })\\n      .catch(err => console.error(err));\\n  };\\n\\n  return (\\n    <div style={{ padding: '20px' }}>\\n      <h1>User Input App</h1>\\n      <form onSubmit={handleSubmit}>\\n        <input\\n          type=\\\"text\\\"\\n          placeholder=\\\"Name\\\"\\n          value={name}\\n          onChange={(e) => setName(e.target.value)}\\n        />\\n        <input\\n          type=\\\"text\\\"\\n          placeholder=\\\"Message\\\"\\n          value={message}\\n          onChange={(e) => setMessage(e.target.value)}\\n        />\\n        <button type=\\\"submit\\\">Submit</button>\\n      </form>\\n      <h2>Submitted Inputs</h2>\\n      <ul>\\n        {inputs.map((input, idx) => (\\n          <li key={idx}>{input.name}: {input.message}</li>\\n        ))}\\n      </ul>\\n    </div>\\n  );\\n}\\n\\nexport default App;\\n",
    "frontend/src/App.css": "body { font-family: Arial, sans-serif; }\\nform { margin-bottom: 20px; }\\ninput { margin-right: 10px; padding: 5px; }\\nbutton { padding: 5px 10px; }\\n"
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