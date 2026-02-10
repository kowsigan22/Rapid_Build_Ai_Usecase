from orchestrator.graph import build_graph
from orchestrator.state import BuildState


def main():
    app = build_graph()

    initial_state: BuildState = {
        "user_prompt": "Create a simple  app",
        "generated_code": None,
        "status": "STARTED"
    }

    final_state = app.invoke(initial_state)

    print("Final State:")
    print(final_state)


if __name__ == "__main__":
    main()