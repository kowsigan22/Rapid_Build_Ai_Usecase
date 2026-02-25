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
        venv_path = os.path.join(app_root, "venv")

        if not os.path.exists(venv_path):
            result = subprocess.run(
                ["python", "-m", "venv", "venv"],
                cwd=app_root,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                state["status"] = "EXECUTION_FAILED"
                state["error"] = f"Failed to create virtual environment:\n{result.stderr}"
                return state
            
        venv_python = os.path.join(venv_path, "Scripts", "python.exe")

        if not os.path.exists(venv_python):
            state["status"] = "EXECUTION_FAILED"
            state["error"] = "Virtual environment python executable not found."
            return state
        
        subprocess.run(
        [venv_python, "-m", "pip", "install", "--upgrade", "pip"],
        capture_output=True,
        text=True
        )
        for relative_path, content in generated_files.items():
            file_path = os.path.join(app_root, relative_path)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        working_dir=None
        if state.get("input_file_path"):
                working_dir = os.path.join(app_root, execution_descriptor["working_dir"])

                shutil.copy(
                    state["input_file_path"],
                    os.path.join(working_dir, "data.csv")
        )
        print("check 0")
        working_dir = os.path.join(app_root, execution_descriptor["working_dir"])
        requirements_path = os.path.join(working_dir, "requirements.txt")
        print("check 1")
        if os.path.exists(requirements_path):
            print("check 1.1")
            install_result = subprocess.run(
                [venv_python, "-m", "pip", "install", "-r", requirements_path],
                cwd=working_dir,
                capture_output=True,
                text=True
            )

            if install_result.returncode != 0:
                state["status"] = "EXECUTION_FAILED"
                state["error"] = f"Dependency installation failed:\n{install_result.stderr}"
                return state

        # 2. Run server
        print("check 2")
        working_dir = os.path.join(app_root, execution_descriptor["working_dir"])
        dir=execution_descriptor["working_dir"]
        if not os.path.isdir(working_dir):
            state["status"] = "EXECUTION_FAILED"
            state["error"] = f"Working directory does not exist: {working_dir}"
            return state
        run_command = execution_descriptor["run"]
        print("check 3")
        if f"{dir}." in run_command:
            run_command = run_command.replace(f"{dir}.", "")
            state["execution_descriptor"]["run"] = run_command
        is_long_running = execution_descriptor["long_running"]
        print("check 4")
        build_cmd = execution_descriptor.get("build")
        # if "uvicorn" in run_command:
        #     parts = run_command.split()
        #     module_part = parts[1]  # main:app
        #     module_name = module_part.split(":")[0]
        #     expected_file = os.path.join(working_dir, f"{module_name}.py")

        #     if not os.path.exists(expected_file):
        #         state["status"] = "EXECUTION_FAILED"
        #         state["error"] = f"Entry file not found: {expected_file}"
        #         return state
        print("check 4")
        requirements_path = os.path.join(working_dir, "requirements.txt")

        
        working_dir = os.path.join(app_root, execution_descriptor["working_dir"])
        print("check 5")
        if build_cmd:
            build_result = subprocess.run(
                build_cmd.split(),
                cwd=working_dir,
                capture_output=True,
                text=True,
                timeout=300
            )
            if build_result.returncode != 0:
                print("Build failed")
                state["status"] = "EXECUTION_FAILED"
                state["error"] = build_result.stderr
                return state
        print("check 6")
        working_dir = os.path.join(app_root, execution_descriptor["working_dir"])

        if is_long_running:
            print("long_running")
            process = subprocess.Popen(
                [venv_python, "-m"] + run_command.split(),
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
            exposed_urls = "http://localhost:8000" for port in ports]

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