import sys
import subprocess
import streamlit as st
import pandas as pd
import io
from pathlib import Path

# Add project root to PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st
import tempfile
from orchestrator.graph import build_graph
from orchestrator.state import BuildState
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Rapid Build AI", layout="wide")

st.title("🚀 Rapid Build AI")
st.write("Generate, validate, and execute Python apps using AI agents")

# --- USER INPUT ---
user_prompt = st.text_area(
    "Describe the Python app you want",
    placeholder="Create a Python app that loads a CSV and prints row count"
)

uploaded_file = st.file_uploader(
    "Upload CSV file (optional)",
    type=["csv"]
)

run_button = st.button("Build & Run")

# --- EXECUTION ---
if run_button and user_prompt.strip():
    with st.spinner("Running AI agents..."):
        temp_file_path = None

        if uploaded_file:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as f:
                f.write(uploaded_file.getbuffer())
                temp_file_path = f.name

        app = build_graph()

        initial_state: BuildState = {
            "user_prompt": user_prompt,
            "generated_files": None,
            "status": "STARTED",
            "retry_count": 0,
            "error": None,
            "error_context": None,
            "exposed_urls": None,
            "input_file_path": temp_file_path,
            "execution_output": None,
            "execution_descriptor": None

        }

        final_state = app.invoke(initial_state)

    st.success("Workflow completed")

    # --- OUTPUT ---
    st.subheader("📌 Final Status")
    st.code(final_state["status"])

    if final_state.get("generated_code"):
        st.subheader("🧠 Generated Code")
        st.code(final_state["generated_code"], language="python")
    
    if final_state.get("error"):
        st.subheader("❌ Error")
        st.code(final_state["error"])
        
    st.write("RAW OUTPUT REPR:", repr(final_state.get("execution_output")))
    st.subheader("▶ Execution Output")

    output = final_state.get("execution_output")
    if output is None:
        st.text("No output captured")
    elif output == "":
        st.text("(Program produced no stdout/stderr)")
    else:
        st.text(output)
    if final_state["status"] == "HEALTHCHECK_PASSED":
        st.success("Application is running")

        exposed_urls = final_state.get("exposed_urls", [])

        if exposed_urls:
            st.subheader("🌐 Exposed APIs / Services")

            for ep in exposed_urls:
                col1, col2 = st.columns([1, 4])
                col1.write(f"**{ep['method']}**")
                col2.markdown(f"[{ep['url']}]({ep['url']})")

        else:
            st.info("No exposed URLs reported by healthcheck")
    st.divider()
st.header("🖥️ System Process Monitor")

# ---------------------------------------------------
# 1️⃣ SHOW ALL RUNNING PROCESSES
# ---------------------------------------------------

if st.button("🔍 Show All Running Processes"):

    result = subprocess.run(
        ["tasklist", "/V", "/FO", "CSV"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        df = pd.read_csv(io.StringIO(result.stdout))

        # Try to detect runtime from process name
        def detect_runtime(name):
            name = str(name).lower()
            if "python" in name:
                return "Python"
            elif "java" in name:
                return "Java"
            elif "node" in name:
                return "Node.js"
            elif "dotnet" in name or "w3wp" in name:
                return ".NET / C#"
            elif "nginx" in name:
                return "Nginx"
            elif "mysql" in name:
                return "MySQL"
            else:
                return "Unknown"

        df["Runtime"] = df["Image Name"].apply(detect_runtime)

        display_df = df[[
            "Image Name",
            "PID",
            "Session Name",
            "Mem Usage",
            "CPU Time",
            "Status",
            "Runtime"
        ]]

        st.dataframe(display_df, use_container_width=True)

    else:
        st.error("Failed to fetch processes")
    st.subheader("🌐 Check Running App by Port")

st.subheader("🌐 Check Running App by Port")

port_input = st.text_input("Enter Port Number (e.g., 8000)")

if st.button("Check Port"):

    if not port_input.strip():
        st.warning("Please enter a port number")
    else:
        result = subprocess.run(
            ["netstat", "-ano"],
            capture_output=True,
            text=True
        )

        lines = result.stdout.splitlines()

        # Filter lines for this port
        matching_lines = [
            line for line in lines if f":{port_input}" in line
        ]

        if not matching_lines:
            st.success(f"Port {port_input} is free.")
        else:
            # Extract UNIQUE PIDs
            pids = set(line.strip().split()[-1] for line in matching_lines)

            for pid in pids:

                st.markdown(f"### 🧩 Application using port {port_input}")
                st.write(f"**PID:** {pid}")

                # Show all connections for this PID
                matching_lines = [
    line for line in lines
    if f":{port_input}" in line and "LISTENING" in line
]

                with st.expander("Show Connections"):
                    for line in matching_lines:
                        st.code(line)

                # Single kill button per PID
                if st.button(
                    f"❌ Kill PID {pid}",
                    key=f"kill_port_{port_input}_{pid}"
                ):
                    subprocess.run(
                        ["taskkill", "/PID", pid, "/F"],
                        capture_output=True
                    )
                    st.success(f"Killed process {pid}")
elif run_button:
    st.warning("Please enter a prompt")