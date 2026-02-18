from orchestrator.state import BuildState


def validation_agent(state: BuildState) -> BuildState:
    files = state.get("generated_files", {})
    desc = state.get("execution_descriptor")

    if not files or "backend/main.py" not in files:
        state["status"] = "INVALID"
        state["error"] = "FastAPI main.py missing"
        return state

    if not desc or "uvicorn" not in desc.get("run", ""):
        state["status"] = "INVALID"
        state["error"] = "Invalid execution descriptor"
        return state

    state["status"] = "VALID"
    return state