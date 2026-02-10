from orchestrator.state import BuildState
from orchestrator.llm import call_llm

def clean_code(code: str) -> str:
    if code.startswith("```"):
        code = code.strip().strip("```")
        code = code.replace("python", "", 1).strip()
    return code


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
        state["generated_code"] = clean_code(code)
        state["status"] = "CODE_GENERATED"
    except Exception as e:
        state["status"] = "LLM_ERROR"
        state["error"] = str(e)

    return state