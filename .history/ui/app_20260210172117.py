import sys
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
    if final_state["status"] == "RUNNING":
        st.success("Backend is running")
        st.markdown("🔗 http://localhost:8000")
elif run_button:
    st.warning("Please enter a prompt")