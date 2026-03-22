from orchestrator.state import BuildState

def error_prompt_agent(state: BuildState) -> BuildState:
    error = state.get("error")

    state["error_context"] = f"""
The previous code failed with this runtime error:

{error}

Fix the issue and regenerate the FULL corrected Python script.
"""
    state["status"] = "REPAIRING"
    return state