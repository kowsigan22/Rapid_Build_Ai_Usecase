import subprocess
import os

def build_agent(state: BuildState) -> BuildState:
    backend_dir = os.path.join("generated_apps/app_001", "backend")

    subprocess.run(
        ["pip", "install", "-r", "requirements.txt"],
        cwd=backend_dir,
        capture_output=True,
        text=True
    )

    state["status"] = "BUILT"
    return state