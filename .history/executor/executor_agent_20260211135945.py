import os
import subprocess
import tempfile
import shutil
from orchestrator.state import BuildState

BASE_DIR = "generated_apps/app_001"

def execution_agent(state: BuildState) -> BuildState:
    try:
        generated_files = state["generated_files"]
        execution_descriptor = state["execution_descriptor"]

        # --- Create app directory ---
        app_id = f"app_{uuid.uuid4().hex[:8]}"
        app_root = os.path.join(BASE_APPS_DIR, app_id)
        os.makedirs(app_root, exist_ok=True)

        # --- Write generated files ---
        for relative_path, content in generated_files.items():
            file_path = os.path.join(app_root, relative_path)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        
        if state.get("input_file_path"):
                shutil.copy(
                    state["input_file_path"],
                    os.path.join(work_dir, "data.csv")  # LLM assumes this name
                )

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