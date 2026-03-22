import os
import subprocess
import tempfile
import shutil
import uuid
from orchestrator.state import BuildState

BASE_APPS_DIR = "generated_apps"

# def run_command(command: str, cwd: str, timeout: int | None = None):
#     return subprocess.run(
#         command.split(),
#         cwd=cwd,
#         capture_output=True,
#         text=True,
#         timeout=timeout
#     )

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
                
        if state.get("input_file_path"):
                working_dir = os.path.join(app_root, execution_descriptor["working_dir"])

                shutil.copy(
                    state["input_file_path"],
                    os.path.join(working_dir, "data.csv")
)

        # 2. Run server
        working_dir = os.path.join(app_root, execution_descriptor["working_dir"])
        if not os.path.isdir(working_dir):
            state["status"] = "EXECUTION_FAILED"
            state["error"] = f"Working directory does not exist: {working_dir}"
            return state
        run_command = execution_descriptor["run"]
        if f"{execution_descriptor["working_dir"]}." in run_command:
            run_command = run_command.replace(f"{working_dir}.", "")
            state["execution_descriptor"]["run"] = run_command
        is_long_running = execution_descriptor["long_running"]
        
        build_cmd = execution_descriptor.get("build")
        if "uvicorn" in run_command:
            parts = run_command.split()
            module_part = parts[1]  # main:app
            module_name = module_part.split(":")[0]
            expected_file = os.path.join(working_dir, f"{module_name}.py")

            if not os.path.exists(expected_file):
                state["status"] = "EXECUTION_FAILED"
                state["error"] = f"Entry file not found: {expected_file}"
                return state
            
        requirements_path = os.path.join(working_dir, "requirements.txt")

        if os.path.exists(requirements_path):
            install_result = subprocess.run(
                ["pip", "install", "-r", "requirements.txt"],
                cwd=working_dir,
                capture_output=True,
                text=True
            )

            if install_result.returncode != 0:
                state["status"] = "EXECUTION_FAILED"
                state["error"] = install_result.stderr
                return state
        
        if build_cmd:
            build_result = subprocess.run(
                build_cmd.split(),
                cwd=working_dir,
                capture_output=True,
                text=True,
                timeout=300
            )
            if build_result.returncode != 0:
                state["status"] = "EXECUTION_FAILED"
                state["error"] = build_result.stderr
                return state
        
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
            ports = execution_descriptor.get("ports", [])
            exposed_urls = [f"http://localhost:{port}" for port in ports]

            state["exposed_urls"] = exposed_urls
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


    except Exception as e:
        state["status"] = "EXECUTION_ERROR"
        state["execution_output"] = str(e)
        state["error"] = str(e)

    return state