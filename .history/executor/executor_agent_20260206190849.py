import subprocess
import tempfile
from orchestrator.state import BuildState


def execution_agent(state: BuildState) -> BuildState:
    """
    Executes generated Python code safely.
    """

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

        if result.returncode == 0:
            state["status"] = "EXECUTED"
        else:
            state["status"] = "EXECUTION_FAILED"

        state["execution_output"] = result.stdout + result.stderr

    except Exception as e:
        state["status"] = "EXECUTION_ERROR"
        state["execution_output"] = str(e)

    return state