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

    max_attempts = 5
    delay = 3

    for attempt in range(max_attempts):
        try:
            all_passed = True

            for ep in endpoints:
                url = base_url + ep["path"]
                method = ep["method"].upper()
                expected = ep["expected_status"]
                payload = ep.get("payload", None)  # Handle optional payload

                if method == "GET":
                    response = requests.get(url, timeout=5)
                elif method == "POST":
                    if payload is None:
                        state["status"] = "HEALTHCHECK_FAILED"
                        state["error"] = f"Missing payload for POST method at {url}"
                        return state
                    response = requests.post(url, json=payload, timeout=5)
                else:
                    state["status"] = "HEALTHCHECK_FAILED"
                    state["error"] = f"Unsupported method {method} for {url}"
                    return state

                if response.status_code != expected:
                    all_passed = False
                    state["status"] = "HEALTHCHECK_FAILED"
                    state["error"] = f"{url} returned status {response.status_code}. Expected {expected}"
                    return state

            if all_passed:
                state["status"] = "HEALTHCHECK_PASSED"
                return state

        except Exception as e:
            state["status"] = "HEALTHCHECK_FAILED"
            state["error"] = f"Healthcheck failed during attempt {attempt + 1}: {str(e)}"
            return state

        time.sleep(delay)

    state["status"] = "HEALTHCHECK_FAILED"
    state["error"] = "Healthcheck failed after maximum retries"
    return state