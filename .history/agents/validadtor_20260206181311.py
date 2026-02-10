from orchestrator.state import BuildState


def validation_agent(state: BuildState) -> BuildState:
    """
    Simulates validation of generated code.
    """

    code = state.get("generated_code")

    if code and "ML" in code:
        state["status"] = "VALID"
    else:
        state["status"] = "INVALID"

    return state