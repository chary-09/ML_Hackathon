import json
import os

def log_user_data(data, log_file="outputs/logs.json"):
    """Logs the user's prediction data to a JSON file."""
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:
            json.dump([], f)

    with open(log_file, "r") as f:
        logs = json.load(f)

    logs.append(data)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)

def get_user_history(log_file="outputs/logs.json"):
    """Reads user prediction history from a JSON file."""
    if not os.path.exists(log_file):
        return []
    with open(log_file, "r") as f:
        return json.load(f)
