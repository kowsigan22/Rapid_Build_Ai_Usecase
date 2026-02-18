import subprocess
import tempfile
import shutil
from orchestrator.state import BuildState


def execution_agent(state: BuildState) -> BuildState:
    try:
        for path, content in state["generated_files"].items():
        full_path = os.path.join(BASE_DIR, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        # 2. Run server
        desc = state["execution_descriptor"]
        work_dir = os.path.join(BASE_DIR, desc["working_dir"])

        subprocess.Popen(
            desc["run"].split(),
            cwd=work_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        state["status"] = "RUNNING"
        state["execution_output"] = "FastAPI running at http://localhost:8000"


    except Exception as e:
        state["status"] = "EXECUTION_ERROR"
        state["execution_output"] = str(e)
        state["error"] = str(e)

    return state