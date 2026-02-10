import subprocess
import tempfile
from orchestrator.state import BuildState


def execution_agent(state: BuildState) -> BuildState:
    code = state.get("generated_code")

    try:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False
        ) as f:
            f.write(code)
            file_path = f.name

        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        state["execution_output"] = result.stdout + result.stderr

        if result.returncode == 0:
            state["status"] = "EXECUTED"
        else:
            state["status"] = "EXECUTION_FAILED"
            state["error"] = result.stderr

    except Exception as e:
        state["status"] = "EXECUTION_ERROR"
        state["error"] = str(e)

    return state