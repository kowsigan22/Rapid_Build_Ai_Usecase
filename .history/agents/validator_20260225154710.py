from orchestrator.state import BuildState


def validation_agent(state: BuildState) -> BuildState:
    generated_files = state.get("generated_files")
    execution_descriptor = state.get("execution_descriptor")

    # --- Basic presence checks ---
    if not generated_files or not isinstance(generated_files, dict):
        state["status"] = "INVALID"
        state["error"] = "generated_files missing or invalid"
        return state

    if not execution_descriptor or not isinstance(execution_descriptor, dict):
        state["status"] = "INVALID"
        state["error"] = "execution_descriptor missing or invalid"
        return state

    # --- Execution descriptor validation ---
    required_exec_fields = [
        "language",
        "working_dir",
        "run",
        "long_running"
    ]

    for field in required_exec_fields:
        if field not in execution_descriptor:
            state["status"] = "INVALID"
            state["error"] = f"execution_descriptor missing required field: {field}"
            return state

    # --- Working directory must exist in generated files ---
    working_dir = execution_descriptor["working_dir"].rstrip("/")
    print("inside validator agent")
    has_working_dir = any(
        path.startswith(f"{working_dir}/") or path == working_dir
        for path in generated_files.keys()
    )
    print("inside validator agent")
    if not has_working_dir:
        print("working directory found in generated files")
        state["status"] = "INVALID"
        state["error"] = f"working_dir '{working_dir}' not found in generated_files"
        return state

    # --- Minimum runnable file check (language-aware, but generic) ---
    language = execution_descriptor["language"].lower()

    if language == "python":
        has_entry = any(
            path.endswith(".py") and path.startswith(working_dir)
            for path in generated_files.keys()
        )
        if not has_entry:
            state["status"] = "INVALID"
            state["error"] = "No Python entry file found in working_dir"
            return state

    elif language == "java":
        has_entry = any(
            path.endswith(".java") and path.startswith(working_dir)
            for path in generated_files.keys()
        )
        if not has_entry:
            state["status"] = "INVALID"
            state["error"] = "No Java source file found in working_dir"
            return state

    elif language in ("javascript", "typescript"):
        has_entry = any(
            path.endswith((".js", ".ts", ".jsx", ".tsx")) and path.startswith(working_dir)
            for path in generated_files.keys()
        )
        if not has_entry:
            state["status"] = "INVALID"
            state["error"] = "No JS/TS entry file found in working_dir"
            return state

    # --- Long-running apps must expose ports ---
    if execution_descriptor["long_running"]:
        ports = execution_descriptor.get("ports")
        if not ports or not isinstance(ports, list):
            state["status"] = "INVALID"
            state["error"] = "long_running application must declare ports"
            return state

    # --- Passed all checks ---
    state["status"] = "VALID"
    return state