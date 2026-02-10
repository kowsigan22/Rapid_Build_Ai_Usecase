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