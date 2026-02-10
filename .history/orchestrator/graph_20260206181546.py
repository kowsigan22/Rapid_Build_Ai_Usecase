from langgraph.graph import StateGraph, END
from orchestrator.state import BuildState
from agents.code_generator import code_generator_agent


def build_graph():
    graph = StateGraph(BuildState)

    graph.add_node("code_generator", code_generator_agent)
    graph.add_node("validator", validation_agent)
    graph.add_node("retry", retry_agent)

    graph.set_entry_point("code_generator")

    graph.add_edge("code_generator", "validator")

    graph.add_conditional_edges(
        "validator",
        route_after_validation,
        {
            END: END,
            "retry": "retry"
        }
    )

    graph.add_edge("retry", END)

    return graph.compile()