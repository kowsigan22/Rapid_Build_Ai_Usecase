from langgraph.graph import StateGraph, END
from orchestrator.state import BuildState
from agents.code_generator import code_generator_agent


def build_graph():
    graph = StateGraph(BuildState)

    # Register agent node
    graph.add_node("code_generator", code_generator_agent)

    # Entry point
    graph.set_entry_point("code_generator")

    # End after code generation (for now)
    graph.add_edge("code_generator", END)

    return graph.compile()