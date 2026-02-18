from typing import Any, TypedDict, Optional

class BuildState(TypedDict):
    user_prompt: str

    # Generated project
    generated_files: Optional[Dict[str, str]]

    # Execution
    execution_descriptor: Optional[Dict[str, Any]]
    execution_output: Optional[str]

    # Control
    status: str
    retry_count: int
    error: Optional[str]
    error_context: Optional[str]