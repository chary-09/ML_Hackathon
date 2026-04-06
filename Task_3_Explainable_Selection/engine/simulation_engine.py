"""
Simulation Engine — What-If Analysis
Simulates how changing individual student behaviors would affect burnout prediction.
"""

import pandas as pd


def run_simulation(data_dict, predict_fn, current_score):
    """
    Simulate improvement scenarios by adjusting one feature at a time.

    Args:
        data_dict: dict with current feature values
        predict_fn: function that takes [list of values] and returns (prediction, prob_dict, score, message)
        current_score: current burnout score

    Returns:
        list of scenario dicts with keys: feature, change, new_score, improvement, description
    """

    scenarios = []

    # Define improvement simulations for each feature
    simulations = {
        "attendance": {
            "improvements": [70, 80, 90],
            "label": "Attendance %",
            "direction": "increase",
            "condition": lambda current, target: current < target
        },
        "study_hours": {
            "improvements": [4, 6, 8],
            "label": "Study Hours",
            "direction": "optimize",
            "condition": lambda current, target: True  # always simulate
        },
        "assignment_delay": {
            "improvements": [0, 1, 2],
            "label": "Assignment Delay",
            "direction": "reduce",
            "condition": lambda current, target: current > target
        },
        "lms_usage": {
            "improvements": [5, 7, 9],
            "label": "LMS Usage",
            "direction": "increase",
            "condition": lambda current, target: current < target
        },
        "performance": {
            "improvements": [60, 75, 90],
            "label": "Performance Score",
            "direction": "increase",
            "condition": lambda current, target: current < target
        }
    }

    feature_order = ["attendance", "study_hours", "assignment_delay", "lms_usage", "performance"]

    for feature in feature_order:
        sim = simulations[feature]
        current_val = data_dict[feature]

        for target_val in sim["improvements"]:
            # Only simulate if the change is meaningful
            if not sim["condition"](current_val, target_val):
                continue

            # Build modified data
            modified = data_dict.copy()
            modified[feature] = target_val
            modified_list = [modified[f] for f in feature_order]

            try:
                _, _, new_score, new_message = predict_fn(modified_list)

                improvement = round(current_score - new_score, 2)

                if improvement > 0:
                    scenarios.append({
                        "feature": sim["label"],
                        "current": current_val,
                        "target": target_val,
                        "direction": sim["direction"],
                        "new_score": new_score,
                        "improvement": improvement,
                        "description": f"If {sim['label']} changes to {target_val}, burnout score drops by {improvement}%"
                    })
            except Exception:
                continue

    # Sort by biggest improvement
    scenarios.sort(key=lambda x: x["improvement"], reverse=True)

    return scenarios[:6]  # Return top 6 most impactful scenarios
