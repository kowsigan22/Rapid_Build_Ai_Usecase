from orchestrator.state import BuildState


def code_generator_agent(state: BuildState) -> BuildState:
    prompt = state["user_prompt"]
    retries = state["retry_count"]

    generated_code = (
        f"# Code generated for prompt: {prompt}\n"
        f"# Retry attempt: {retries}"
    )

    state["generated_code"] = generated_code
    state["status"] = "CODE_GENERATED"

    return state