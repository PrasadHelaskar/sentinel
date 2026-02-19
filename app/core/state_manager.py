import json
import os

STATE_FILE = "data/processed_runs.json"

class StateManager:

    @staticmethod
    def load():
        if not os.path.exists(STATE_FILE):
            return {}

        with open(STATE_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save(state):
        os.makedirs("data", exist_ok=True)
        with open(STATE_FILE, "w") as f:
            json.dump(state, f, indent=2)

    @staticmethod
    def is_processed(repo, run_id):
        state = StateManager.load()
        return str(run_id) in state.get(repo, [])

    @staticmethod
    def mark_processed(repo, run_id):
        state = StateManager.load()
        state.setdefault(repo, []).append(str(run_id))
        StateManager.save(state)
