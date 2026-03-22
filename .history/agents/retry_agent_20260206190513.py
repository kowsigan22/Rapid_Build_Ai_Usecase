from orchestrator.state import BuildState


    
MAX_RETRIES = 3


def retry_agent(state: BuildState) -> BuildState:
    state["retry_count"] += 1

    if state["retry_count"] >= MAX_RETRIES:
        state["status"] = "FAILED"
    else:
        state["status"] = "RETRYING"

    return state