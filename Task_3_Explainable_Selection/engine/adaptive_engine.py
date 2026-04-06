import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "outputs", "logs.json")


def save_log(data, prediction, score):
    log_entry = {
        "data": data,
        "prediction": prediction,
        "burnout_score": score,
        "timestamp": str(datetime.now())
    }

    # Create folder if not exists
    output_dir = os.path.dirname(LOG_FILE)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load existing logs
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except Exception:
            logs = []

    logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


def load_logs():
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []
    return []
