from langgraph.graph import StateGraph, END
from orchestrator.state import BuildState
from agents.code_generator import code_generator_agent
from agents.validator import validation_agent
from agents.retry_agent import retry_agent
from executor.executor_agent import execution_agent


def route_after_validation(state: BuildState):
    if state["status"] == "VALID":
        return "execute"
    return "retry"


def route_after_retry(state: BuildState):
    if state["status"] == "FAILED":
        return END
    return "code_generator"


def build_graph():
    graph = StateGraph(BuildState)

    graph.add_node("code_generator", code_generator_agent)
    graph.add_node("validator", validation_agent)
    graph.add_node("retry", retry_agent)
    graph.add_node("execute", execution_agent)

    graph.set_entry_point("code_generator")

    graph.add_edge("code_generator", "validator")

    graph.add_conditional_edges(
        "validator",
        route_after_validation,
        {
            "execute": "execute",
            "retry": "retry"
        }
    )

    graph.add_conditional_edges(
        "retry",
        route_after_retry,
        {
            "code_generator": "code_generator",
            END: END
        }
    )

    graph.add_edge("execute", END)

    return graph.compile()