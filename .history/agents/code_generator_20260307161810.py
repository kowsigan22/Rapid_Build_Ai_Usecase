from orchestrator.state import BuildState
from orchestrator.llm import call_llm
import json
import re





def load_prompt(path: str, state: BuildState) -> str:
    with open(path) as f:
        template = f.read()

    return (
        template
        .replace("{{user_prompt}}", state["user_prompt"])
        .replace("{{error_context}}", state.get("error_context") or "")
    )

def repair_llm_json(raw_output: str):
    if not raw_output:
        raise ValueError("LLM output is empty")

    text = raw_output.strip()

    # Remove triple quotes if present
    if text.startswith('"""') and text.endswith('"""'):
        text = text[3:-3].strip()

    # Extract JSON block
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in LLM output")

    text = match.group(0)

    # Fix broken decorators like:
    # @app.get
    # ("/")
    text = re.sub(r'@\w+\.\w+\s*\n\s*\(', r'@\g<0>'.replace("\n", ""), text)

    # Fix newline before parentheses
    text = re.sub(r'\n\s*\(', '(', text)

    # Escape newlines inside JSON strings
    def escape_newlines(match):
        content = match.group(0)
        return content.replace("\n", "\\n")

    text = re.sub(r'"(.*?)"', escape_newlines, text, flags=re.DOTALL)

    return json.loads(text)


def code_generator_agent(state: BuildState) -> BuildState:
    prompt = load_prompt("prompts/code_generation.txt", state)
    print("error_context",state["error_context"])
    try:
        code = call_llm(prompt)
        print("LLM OUTPUT >>>", code)
        raw = code.strip()

        match = re.search(r"\{.*\}", raw, re.DOTALL)

        if not match:
            raise ValueError("LLM did not return JSON")

        print("code_generator check 0.2")
        # print("RAW LLM OUTPUT >>>", repr(code))
        payload = repair_llm_json(code)
        print("code_generator check 0.1")
        if "generated_files" not in payload:
            print("code_generator check 0")
            raise ValueError("LLM output missing 'generated_files'")

        if "execution_descriptor" not in payload:
            raise ValueError("LLM output missing 'execution_descriptor'")

        state["generated_files"] = payload["generated_files"]
        print("code_generator check 1")
        print(payload["generated_files"])
        state["execution_descriptor"] = payload["execution_descriptor"]
        state["status"] = "CODE_GENERATED"
    except json.JSONDecodeError as e:
        state["status"] = "LLM_ERROR"
        state["error"] = f"Invalid JSON from LLM: {e}"
        state["error_context"] = code
    except Exception as e:
        state["status"] = "LLM_ERROR"
        state["error"] = str(e)

    # return state
#     state["generated_files"] = {
#         "backend/main.py": """
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "Hello from FastAPI"}
# """,
#         "backend/requirements.txt": """
# fastapi
# uvicorn
# """
#     }

#     state["execution_descriptor"] = {
#         "language": "python",
#         "framework": "fastapi",
#         "working_dir": "backend",
#         "run": "uvicorn main:app --host 0.0.0.0 --port 8000",
#         "long_running": True,
#         "ports": [8000]
#     }

    # state["status"] = "CODE_GENERATED"
    return state