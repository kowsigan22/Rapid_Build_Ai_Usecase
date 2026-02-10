from orchestrator.state import BuildState


def validation_agent(state: BuildState) -> BuildState:
    code = state.get("generated_code")

    if not code:
        state["status"] = "INVALID"
        return state

    if "import" in code and "def" in code:
        state["status"] = "VALID"
    else:
        state["status"] = "INVALID"

    return state