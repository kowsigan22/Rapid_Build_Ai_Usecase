from langgraph.graph import StateGraph, END
from orchestrator.state import BuildState
from agents.code_generator import code_generator_agent
from agents.validator import validation_agent
from agents.retry_agent import retry_agent
from agents.error_prompt_agent import error_prompt_agent
from executor.executor_agent import execution_agent


def route_after_validation(state: BuildState):
    if state["status"] == "VALID":
        return "execute"
    return "error_prompt"

def route_after_execution(state: BuildState):
    if state["status"] == "EXECUTED":
        return END
    return "error_prompt"


def route_after_retry(state: BuildState):
    if state["status"] == "FAILED":
        return END
    return "code_generator"


def build_graph():
    graph = StateGraph(BuildState)

    graph.add_node("code_generator", code_generator_agent)
    graph.add_node("validator", validation_agent)
    graph.add_node("execute", execution_agent)
    graph.add_node("error_prompt", error_prompt_agent)
    graph.add_node("retry", retry_agent)

    graph.set_entry_point("code_generator")

    graph.add_edge("code_generator", "validator")
    
    graph.add_conditional_edges(
        "validator",
        route_after_validation,
        {
            "execute": "execute",
            "error_prompt": "error_prompt"
        }
    )

    graph.add_conditional_edges(
        "execute",
        route_after_execution,
        {
            END: END,
            "error_prompt": "error_prompt"
        }
    )

    graph.add_edge("error_prompt", "retry")

    graph.add_conditional_edges(
        "retry",
        route_after_retry,
        {
            "code_generator": "code_generator",
            END: END
        }
    )

    return graph.compile()