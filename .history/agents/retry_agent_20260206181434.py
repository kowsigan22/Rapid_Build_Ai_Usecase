from orchestrator.state import BuildState


def retry_agent(state: BuildState) -> BuildState:
    """
    Simulates retry logic.
    """

    state["generated_code"] += "\n# Retried with improvements"
    state["status"] = "RETRIED"

    return state