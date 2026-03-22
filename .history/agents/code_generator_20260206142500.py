from orchestrator.state import BuildState


def code_generator_agent(state: BuildState) -> BuildState:
    """
    First dummy agent.
    Later this will call an LLM.
    """

    prompt = state["user_prompt"]

    # Dummy logic for now
    generated_code = f"# Code generated for prompt: {prompt}"

    state["generated_code"] = generated_code
    state["status"] = "CODE_GENERATED"

    return state