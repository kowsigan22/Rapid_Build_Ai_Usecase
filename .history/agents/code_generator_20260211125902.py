from orchestrator.state import BuildState
from orchestrator.llm import call_llm




def load_prompt(path: str, state: BuildState) -> str:
    with open(path) as f:
        template = f.read()

    return (
        template
        .replace("{{user_prompt}}", state["user_prompt"])
        .replace("{{error_context}}", state.get("error_context") or "")
    )


def code_generator_agent(state: BuildState) -> BuildState:
    prompt = load_prompt("prompts/code_generation.txt", state)

    try:
        code = call_llm(prompt)
        state["generated_code"] = code
        state["status"] = "CODE_GENERATED"
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