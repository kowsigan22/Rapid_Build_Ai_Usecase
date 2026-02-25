from orchestrator.state import BuildState

def error_prompt_agent(state: BuildState) -> BuildState:
    error = state.get("error")
    print()
    state["error_context"] = f"""
The previous code failed with this runtime error:

{error}

Fix project structure, dependencies, or run command.
"""
    state["status"] = "REPAIRING"
    return state