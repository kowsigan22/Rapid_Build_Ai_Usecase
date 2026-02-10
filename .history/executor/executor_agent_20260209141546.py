import subprocess
import tempfile
import shutil
from orchestrator.state import BuildState


def execution_agent(state: BuildState) -> BuildState:
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Write generated code
            code_path = f"{temp_dir}/app.py"
            with open(code_path, "w") as f:
                f.write(state["generated_code"])

            # Copy uploaded file if exists
            if state.get("input_file_path"):
                shutil.copy(
                    state["input_file_path"],
                    f"{temp_dir}/data.csv"  # LLM assumes this name
                )

            result = subprocess.run(
                ["python", code_path],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=temp_dir
            )

            state["execution_output"] = result.stdout + result.stderr

            if result.returncode == 0:
                state["status"] = "EXECUTED"
            else:
                state["status"] = "EXECUTION_FAILED"
                state["error"] = result.stderr

    except Exception as e:
        state["status"] = "EXECUTION_ERROR"
        state["execution_output"] = str(e)
        state["error"] = str(e)

    return state