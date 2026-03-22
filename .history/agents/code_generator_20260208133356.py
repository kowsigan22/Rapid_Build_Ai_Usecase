from orchestrator.state import BuildState
from orchestrator.llm import call_llm


def load_prompt(template_path: str, user_prompt: str) -> str:
    with open(template_path, "r") as f:
        template = f.read()
    return template.replace("{{user_prompt}}", user_prompt)


def code_generator_agent(state: BuildState) -> BuildState:
    user_prompt = state["user_prompt"]
    retry_count = state["retry_count"]

    prompt = load_prompt(
        "prompts/code_generation.txt",
        user_prompt
    )

    try:
        code = call_llm(prompt)
        print("LLM OUTPUT:\n", code) 
        state["generated_code"] = code
        state["status"] = "CODE_GENERATED"
    except Exception as e:
        print("LLM ERROR:", e)
        state["generated_code"] = None
        state["status"] = "LLM_ERROR"
        state["error"] = str(e)

    return state