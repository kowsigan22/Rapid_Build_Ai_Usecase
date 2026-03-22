import os
import subprocess
import tempfile
import shutil
import uuid
from orchestrator.state import BuildState
import time
import requests

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
        os.makedirs(BASE_APPS_DIR, exist_ok=True)
        # --- Create app directory ---
        app_id = f"app_{uuid.uuid4().hex[:8]}"
        app_root = os.path.join(BASE_APPS_DIR, app_id)
        print(app_root)
        os.makedirs(app_root, exist_ok=True)
        working_dir = os.path.join(app_root, execution_descriptor["working_dir"])
        venv_path = os.path.join(app_root, "venv")
        venv_python = os.path.join(venv_path, "Scripts", "python.exe")    

        if not os.path.exists(venv_path):
            result = subprocess.run(
                ["python", "-m", "venv", "venv"],
                cwd=app_root,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                state["status"] = "EXECUTION_FAILED"
                print(f"Failed to create virtual environment:\n{result.stderr}")
                state["error"] = f"Failed to create virtual environment:\n{result.stderr}"
                return state
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
            # if relative_path == "requirements.txt":
            #     relative_path="backend/requirements.txt"
            file_path = os.path.join(app_root, relative_path)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        if state.get("error"):
            state["error"]="Removed previous generated apps error"
        if state.get("input_file_path"):
                working_dir = os.path.join(app_root, execution_descriptor["working_dir"])

                shutil.copy(
                    state["input_file_path"],
                    os.path.join(working_dir, "data.csv")
        )
        
        print("check 0")
        requirements_path = os.path.join(working_dir, "requirements.txt")
    #     with open(requirements_path, "r+", encoding="utf-8") as f:
    #         f.truncate(0)
    #     print("check 1")
    #     requirements = [
    #     "fastapi==0.110.0",
    #     "uvicorn==0.29.0",
    #     "pydantic==2.6.4"
    # ]
    #     with open(requirements_path, "w", encoding="utf-8") as f:
    #         f.write("\n".join(requirements))
        if os.path.exists(requirements_path):
            print("check 1.1")
            install_result = subprocess.run(
                [venv_python, "-m", "pip", "install", "-r", "requirements.txt"],
                cwd=working_dir,
                capture_output=True,
                text=True
            )

            if install_result.returncode != 0:
                state["status"] = "EXECUTION_FAILED"
                print(f"Dependency installation failed:\n{install_result.stderr}")
                state["error"] = f"Dependency installation failed:\n{install_result.stderr}"
                return state
            

        # 2. Run server
        print("check 2")
        dir=execution_descriptor["working_dir"]
        if not os.path.isdir(working_dir):
            state["status"] = "EXECUTION_FAILED"
            state["error"] = f"Working directory does not exist: {working_dir}"
            return state
        run_command = execution_descriptor["run"]
        print("check 3")
        # if f"{dir}." in run_command:
        #     run_command = run_command.replace(f"{dir}.", "")
        #     state["execution_descriptor"]["run"] = run_command
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
        if build_cmd:
            build_result = subprocess.run(
                build_cmd.split(),
                cwd=app_root,
                capture_output=True,
                text=True,
                timeout=300
            )
            if build_result.returncode != 0:
                print("Build failed")
                state["status"] = "EXECUTION_FAILED"
                print("error ",build_result.stderr)
                state["error"] = build_result.stderr
                return state
        print("check 6")
        if "uvicorn" in run_command:
            index = run_command.find("uvicorn")
            result = None

            if index != -1:
                result = run_command[index:]

            if result:
                run_command = f'"{venv_python}" -m {result}'
        if run_command.startswith("python"):
            run_command = run_command.replace("python", f'"{venv_python}"', 1)
        if is_long_running and execution_descriptor["application_type"] == "web-service":
            print("long_running")
            process = subprocess.Popen(
                [venv_python, "-m"] + run_command.split(),
                cwd=app_root,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print("check 7")
            time.sleep(4)

            if process.poll() is not None:
                stderr = process.stderr.read()
                print("check 7.1")
                state["status"] = "EXECUTION_FAILED"
                state["error"] = f"Server crashed immediately:\n{stderr}"
                print("error",stderr)
                return state
            
            try:
                print("Inside doc polling")
                port = execution_descriptor["ports"][0]
                base_url = f"http://localhost:{port}/docs"
                requests.get(base_url, timeout=2)
                print("exciting doc polling")
            except Exception:
                stderr_output = process.stderr.read() if process.stderr else ""

                state["status"] = "EXECUTION_FAILED"
                state["error"] = (
                    "Server process running but application failed to load:\n"
                    f"{stderr_output}"
                )
                return state
            state["execution_output"] = (
                f"Application started (PID={process.pid})\n"
                f"Working dir: {app_root}\n"
                f"Command: {run_command}"
            )
            print("check 8")
            # ports = execution_descriptor.get("ports", [])
            exposed_urls = "http://localhost:8000" 

            state["exposed_urls"] = exposed_urls
            state["status"] = "RUNNING"


        elif execution_descriptor["application_type"] == "batch-job":
            result = subprocess.run(
                run_command.split(),
                cwd=app_root,
                capture_output=True,
                text=True,
                timeout=60
            )

            state["execution_output"] = (result.stdout or "") + (result.stderr or "")
            state["status"] = "EXECUTED"
            
        elif execution_descriptor["application_type"] == "frontend":

            build_cmd = execution_descriptor.get("build")

            if build_cmd:
                build_result = subprocess.run(
                    build_cmd,
                    cwd=app_root,
                    shell=True,
                    capture_output=True,
                    text=True
                )

                if build_result.returncode != 0:
                    state["status"] = "EXECUTION_FAILED"
                    state["error"] = build_result.stderr
                    return state

            process = subprocess.Popen(
                run_command,
                cwd=app_root,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            ports = execution_descriptor.get("ports", [])

            state["exposed_urls"] = [
                {"type": "frontend", "url": f"http://localhost:{p}"}
                for p in ports
            ]

            state["execution_output"] = (
                f"Frontend started (PID={process.pid})\n"
                f"Command: {run_command}"
            )

            state["status"] = "RUNNING"


    except Exception as e:
        print("Inside Exception block")
        state["status"] = "EXECUTION_ERROR"
        print("error ",str(e))
        state["execution_output"] = str(e)
        state["error"] = str(e)
    print(state["error"])
    return state