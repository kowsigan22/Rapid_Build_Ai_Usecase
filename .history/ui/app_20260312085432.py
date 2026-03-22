import sys
import subprocess
import streamlit as st
import pandas as pd
import io
import tempfile

from pathlib import Path
from dotenv import load_dotenv

# --- Add project root ---
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from orchestrator.graph import build_graph
from orchestrator.state import BuildState

load_dotenv()

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(page_title="Rapid Build AI", layout="wide")

st.title("🚀 Rapid Build AI")
st.write("Generate, validate, and execute applications using AI agents")

# ------------------------------------------------
# SESSION STATE INITIALIZATION
# ------------------------------------------------

if "final_state" not in st.session_state:
    st.session_state.final_state = None

if "port_pids" not in st.session_state:
    st.session_state.port_pids = []

if "current_port" not in st.session_state:
    st.session_state.current_port = None


# ------------------------------------------------
# USER INPUT
# ------------------------------------------------

user_prompt = st.text_area(
    "Describe the Python app you want",
    placeholder="Create a FastAPI app with GET and POST endpoints"
)

uploaded_file = st.file_uploader(
    "Upload CSV file (optional)",
    type=["csv"]
)

run_button = st.button("🚀 Build & Run")


# ------------------------------------------------
# BUILD & RUN WORKFLOW
# ------------------------------------------------

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
            "execution_descriptor": None,
            "execution_output": None,
            "exposed_urls": None,
            "input_file_path": temp_file_path,
            "status": "STARTED",
            "retry_count": 0,
            "error": None,
            "error_context": None
        }

        final_state = app.invoke(initial_state)

        # SAVE RESULT
        st.session_state.final_state = final_state


# ------------------------------------------------
# SHOW EXECUTION RESULT (ALWAYS PERSIST)
# ------------------------------------------------

if st.session_state.final_state:

    final_state = st.session_state.final_state

    st.divider()
    st.header("📌 Execution Result")

    st.subheader("Status")
    st.code(final_state["status"])

    if final_state.get("error"):
        st.subheader("Error")
        st.code(final_state["error"])

    st.subheader("Execution Output")

    output = final_state.get("execution_output")

    if output:
        st.text(output)
    else:
        st.info("No execution output captured")


# ------------------------------------------------
# EXPOSED APIS
# ------------------------------------------------
    if final_state["status"] == "EXECUTED":

            st.success("Batch Job Completed")

            st.subheader("🖥 Execution Output")

            output = final_state.get("execution_output")

            if output:
                st.code(output)
            else:
                st.info("No output produced")

    if final_state["status"] == "HEALTHCHECK_PASSED" or final_state["status"] == "RUNNING":

        st.success("Application is running")

        exposed_urls = final_state.get("exposed_urls", [])

        if exposed_urls:

            st.subheader("🌐 Exposed APIs")

            for ep in exposed_urls:

                if ep.get("type") == "frontend":
                    st.markdown(f"🌐 Frontend App → [{ep['url']}]({ep['url']})")

                else:
                    col1, col2 = st.columns([1,4])
                    col1.write(f"**{ep['method']}**")
                    col2.markdown(f"[{ep['url']}]({ep['url']})")

        else:
            st.info("No exposed APIs reported")
    state = st.session_state.get("final_state")

    health = None

    if state:
        descriptor = state.get("execution_descriptor") or {}
        health = descriptor.get("healthcheck")

    if health:

        base_url = health.get("base_url")

        endpoints = health.get("endpoints", [])

        st.subheader("📡 Backend API Specification")

        api_text = f"Base URL:\n{base_url}\n\nEndpoints:\n"

        for ep in endpoints:
            api_text += f"{ep['method']}  {ep['path']}\n"
            if "payload" in ep:
                api_text += "Request Body:\n"
                api_text += f"{json.dumps(ep['payload'], indent=2)}\n"

            api_text += "\n"

        st.code(api_text, language="text")


# ------------------------------------------------
# SYSTEM PROCESS MONITOR
# ------------------------------------------------

st.divider()
st.header("🖥️ System Process Monitor")

if st.button("🔍 Show All Running Processes"):

    result = subprocess.run(
        ["tasklist", "/V", "/FO", "CSV"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:

        df = pd.read_csv(io.StringIO(result.stdout))

        def detect_runtime(name):
            name = str(name).lower()

            if "python" in name:
                return "Python"
            elif "java" in name:
                return "Java"
            elif "node" in name:
                return "Node.js"
            elif "dotnet" in name:
                return ".NET"
            else:
                return "Unknown"

        df["Runtime"] = df["Image Name"].apply(detect_runtime)

        display_df = df[
            ["Image Name","PID","Mem Usage","CPU Time","Status","Runtime"]
        ]

        st.dataframe(display_df, use_container_width=True)

    else:
        st.error("Failed to fetch processes")


# ------------------------------------------------
# PORT CHECK TOOL
# ------------------------------------------------

st.subheader("🌐 Check Running App by Port")

port_input = st.text_input("Enter Port Number (e.g., 8000)")

if st.button("Check Port"):

    result = subprocess.run(
        ["netstat", "-ano"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.splitlines()

    listening_lines = [
        line for line in lines
        if f":{port_input}" in line and "LISTENING" in line
    ]

    if not listening_lines:

        st.session_state.port_pids = []
        st.success(f"Port {port_input} is free")

    else:

        pids = list(set(line.strip().split()[-1] for line in listening_lines))

        st.session_state.port_pids = pids
        st.session_state.current_port = port_input


# ------------------------------------------------
# SHOW PID RESULTS
# ------------------------------------------------

if st.session_state.port_pids:

    for pid in st.session_state.port_pids:

        st.markdown(f"### 🧩 App running on port {st.session_state.current_port}")
        st.write(f"PID: {pid}")

        if st.button(f"❌ Kill PID {pid}", key=f"kill_{pid}"):

            kill_result = subprocess.run(
                ["taskkill", "/PID", pid, "/F", "/T"],
                capture_output=True,
                text=True
            )

            st.write("Return Code:", kill_result.returncode)
            st.code(kill_result.stdout)
            st.code(kill_result.stderr)