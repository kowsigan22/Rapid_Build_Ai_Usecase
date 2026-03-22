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
    respcontentonse = client.chat.completions.create(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.
    return """{
  "generated_files": {
    "frontend/package.json": "{\\n  \\"name\\": \\"react-fastapi-client\\",\\n  \\"version\\": \\"1.0.0\\",\\n  \\"private\\": true,\\n  \\"scripts\\": {\\n    \\"dev\\": \\"vite --port 3000\\",\\n    \\"build\\": \\"vite build\\",\\n    \\"preview\\": \\"vite preview --port 3000\\"\\n  },\\n  \\"dependencies\\": {\\n    \\"react\\": \\"^18.2.0\\",\\n    \\"react-dom\\": \\"^18.2.0\\"\\n  },\\n  \\"devDependencies\\": {\\n    \\"vite\\": \\"^5.0.0\\",\\n    \\"@vitejs/plugin-react\\": \\"^4.0.0\\"\\n  }\\n}",
    "frontend/vite.config.js": "import { defineConfig } from 'vite'\\nimport react from '@vitejs/plugin-react'\\n\\nexport default defineConfig({\\n  plugins: [react()],\\n  server: {\\n    port: 3000\\n  }\\n})",
    "frontend/index.html": "<!DOCTYPE html>\\n<html>\\n<head>\\n  <meta charset='UTF-8'>\\n  <title>React FastAPI Client</title>\\n</head>\\n<body>\\n  <div id='root'></div>\\n  <script type='module' src='/src/main.jsx'></script>\\n</body>\\n</html>",
    "frontend/src/main.jsx": "import React from 'react'\\nimport ReactDOM from 'react-dom/client'\\nimport App from './App.jsx'\\n\\nReactDOM.createRoot(document.getElementById('root')).render(\\n  <React.StrictMode>\\n    <App />\\n  </React.StrictMode>\\n)",
    "frontend/src/api.js": "const BASE_URL = 'http://localhost:8000';\\n\\nexport async function getRoot() {\\n  const res = await fetch(`${BASE_URL}/`);\\n  return res.json();\\n}\\n\\nexport async function getItems() {\\n  const res = await fetch(`${BASE_URL}/items`);\\n  return res.json();\\n}\\n\\nexport async function createItem(data) {\\n  const res = await fetch(`${BASE_URL}/items`, {\\n    method: 'POST',\\n    headers: {\\n      'Content-Type': 'application/json'\\n    },\\n    body: JSON.stringify(data)\\n  });\\n  return res.json();\\n}",
    "frontend/src/App.jsx": "import React, { useEffect, useState } from 'react';\\nimport { getRoot, getItems, createItem } from './api';\\n\\nfunction App() {\\n  const [items, setItems] = useState([]);\\n  const [name, setName] = useState('');\\n  const [price, setPrice] = useState('');\\n  const [status, setStatus] = useState('');\\n\\n  useEffect(() => {\\n    loadRoot();\\n    loadItems();\\n  }, []);\\n\\n  async function loadRoot() {\\n    const res = await getRoot();\\n    setStatus(res.status);\\n  }\\n\\n  async function loadItems() {\\n    const data = await getItems();\\n    setItems(data);\\n  }\\n\\n  async function addItem() {\\n    await createItem({ name, price: parseInt(price) });\\n    setName('');\\n    setPrice('');\\n    loadItems();\\n  }\\n\\n  return (\\n    <div style={{ padding: 20 }}>\\n      <h1>React → FastAPI Demo</h1>\\n\\n      <h3>Backend Status</h3>\\n      <p>{status}</p>\\n\\n      <h3>Create Item</h3>\\n      <input\\n        placeholder='Name'\\n        value={name}\\n        onChange={e => setName(e.target.value)}\\n      />\\n\\n      <input\\n        placeholder='Price'\\n        value={price}\\n        onChange={e => setPrice(e.target.value)}\\n      />\\n\\n      <button onClick={addItem}>Add</button>\\n\\n      <h3>Items</h3>\\n      <ul>\\n        {items.map((item, i) => (\\n          <li key={i}>{item.name} - {item.price}</li>\\n        ))}\\n      </ul>\\n    </div>\\n  );\\n}\\n\\nexport default App;",
    "frontend/README.md": "React client for FastAPI backend"
  },
  "execution_descriptor": {
    "language": "javascript",
    "framework": "react",
    "application_type": "frontend",
    "working_dir": "frontend",
    "build": "npm install",
    "run": "npm run dev",
    "long_running": true,
    "ports": [3000],
    "healthcheck": {
      "base_url": "http://localhost:3000",
      "endpoints": [
        {
          "path": "/",
          "method": "GET",
          "expected_status": 200
        }
      ]
    }
  }
}"""