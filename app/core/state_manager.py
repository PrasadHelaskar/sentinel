import json
import os
from datetime import datetime, timedelta

STATE_FILE = "data/processed_runs.json"
MAX_RUNS_PER_REPO = 10
RETENTION_DAYS = 7

class StateManager:

    @staticmethod
    def _load():
        if not os.path.exists(STATE_FILE):
            return {}

        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Corrupted file safety
            return {}

    @staticmethod
    def _save(state):
        os.makedirs("data", exist_ok=True)

        temp_file = STATE_FILE + ".tmp"
        with open(temp_file, "w") as f:
            json.dump(state, f, indent=2)

        # Atomic replace (CI safe)
        os.replace(temp_file, STATE_FILE)

    @staticmethod
    def is_processed(repo, run_id):
        state = StateManager._load()
        runs = state.get(repo, [])

        return any(r["run_id"] == str(run_id) for r in runs)

    @staticmethod
    def mark_processed(repo, run_id):
        state = StateManager._load()
        repo_runs = state.setdefault(repo, [])

        run_entry = {
            "run_id": str(run_id),
            "processed_at": datetime.utcnow().isoformat()
        }

        # Avoid duplicates
        if not any(r["run_id"] == str(run_id) for r in repo_runs):
            repo_runs.append(run_entry)

        # Cleanup after insert
        StateManager._cleanup_repo(repo, state)

        StateManager._save(state)

    @staticmethod
    def _cleanup_repo(repo, state):
        runs = state.get(repo, [])

        cutoff = datetime.utcnow() - timedelta(days=RETENTION_DAYS)

        # Remove old entries
        filtered = [
            r for r in runs
            if datetime.fromisoformat(r["processed_at"]) > cutoff
        ]

        # Keep only last N runs
        filtered = filtered[-MAX_RUNS_PER_REPO:]

        state[repo] = filtered


        #Butter_149
        