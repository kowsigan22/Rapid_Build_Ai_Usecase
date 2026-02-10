from orchestrator.graph import build_graph
from orchestrator.state import BuildState
from dotenv import load_dotenv
load_dotenv()


def main():
    app = build_graph()

    initial_state: BuildState = {
        "user_prompt": "Create a simple ML app",
        "generated_code": None,
        "status": "STARTED",
        "retry_count": 0
    }

    final_state = app.invoke(initial_state)

    print("Final State:")
    for k, v in final_state.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()