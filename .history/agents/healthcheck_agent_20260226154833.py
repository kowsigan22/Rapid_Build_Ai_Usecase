import requests
import time
from orchestrator.state import BuildState


def healthcheck_agent(state: BuildState) -> BuildState:
    descriptor = state["execution_descriptor"]
    health = descriptor.get("healthcheck")

    if not health:
        state["status"] = "HEALTHCHECK_FAILED"
        state["error"] = "Missing healthcheck configuration"
        return state

    base_url = health["base_url"]
    endpoints = health["endpoints"]

    time.sleep(3)

    for ep in endpoints:
        url = base_url + ep["path"]
        method = ep["method"].upper()
        expected = ep["expected_status"]

        try:
            if method == "GET":
                response = requests.get(url)
            elif method == "POST":
                response = requests.post(url, json={})
            else:
                state["status"] = "HEALTHCHECK_FAILED"
                state["error"] = f"Unsupported method {method}"
                return state

            if response.status_code != expected:
                state["status"] = "HEALTHCHECK_FAILED"
                state["error"] = f"{url} returned {response.status_code}"
                return state

        except Exception as e:
            state["status"] = "HEALTHCHECK_FAILED"
            state["error"] = str(e)
            return state

    state["status"] = "HEALTHCHECK_PASSED"
    return state