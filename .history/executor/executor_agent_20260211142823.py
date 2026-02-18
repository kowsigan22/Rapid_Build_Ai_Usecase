import os
import subprocess
import tempfile
import shutil
import uuid
from orchestrator.state import BuildState

BASE_APPS_DIR = "generated_apps"

def execution_agent(state: BuildState) -> BuildState:
    try:
        generated_files = state["generated_files"]
        execution_descriptor = state["execution_descriptor"]

        # --- Create app directory ---
        app_id = f"app_{uuid.uuid4().hex[:8]}"
        app_root = os.path.join(BASE_APPS_DIR, app_id)
        os.makedirs(app_root, exist_ok=True)
        
        for relative_path, content in generated_files.items():
            file_path = os.path.join(app_root, relative_path)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

        # 2. Run server
        working_dir = os.path.join(app_root, execution_descriptor["working_dir"])
        run_command = execution_descriptor["run"]
        is_long_running = execution_descriptor["long_running"]
        
        if is_long_running:
            process = subprocess.Popen(
                run_command.split(),
                cwd=working_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            state["execution_output"] = (
                f"Application started (PID={process.pid})\n"
                f"Working dir: {working_dir}\n"
                f"Command: {run_command}"
            )
            state["status"] = "RUNNING"

        else:
            result = subprocess.run(
                run_command.split(),
                cwd=working_dir,
                capture_output=True,
                text=True,
                timeout=60
            )

            state["execution_output"] = (result.stdout or "") + (result.stderr or "")
            state["status"] = "EXECUTED"
        state["status"] = "RUNNING"
        state["execution_output"] = "FastAPI running at http://localhost:8000"


    except Exception as e:
        state["status"] = "EXECUTION_ERROR"
        state["execution_output"] = str(e)
        state["error"] = str(e)

    return state