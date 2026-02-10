from typing import TypedDict, Optional


class BuildState(TypedDict):
    user_prompt: str
    generated_code: Optional[str]
    status: str