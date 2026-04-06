"""
Explainability Engine — SHAP-based feature attribution
Provides mathematical explanation of WHY a student received a specific burnout prediction.
"""

import numpy as np

try:
    import shap
    SHAP_AVAILABLE = True
except ImportError:
    SHAP_AVAILABLE = False


def explain_prediction(model, model_name, data_df, feature_names, X_train=None):
    """
    Generate SHAP-based explanations for a single prediction.
    
    Returns:
        dict with:
            - shap_values: dict of {feature_name: shap_value} for the predicted class
            - top_factors: list of human-readable strings explaining top contributors
            - available: bool indicating if SHAP was successfully computed
    """

    result = {
        "shap_values": {},
        "top_factors": [],
        "available": False
    }

    if not SHAP_AVAILABLE:
        result["top_factors"] = ["SHAP library not installed. Run: pip install shap"]
        return result

    try:
        # Choose the right explainer based on model type
        if model_name in ["Random Forest", "Gradient Boosting"]:
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(data_df)
        else:
            # Logistic Regression — use LinearExplainer
            explainer = shap.LinearExplainer(model, X_train)
            shap_values = explainer.shap_values(data_df)

        # Get prediction class index
        prediction = model.predict(data_df)[0]

        # Handle multi-class SHAP output
        if isinstance(shap_values, list):
            # shap_values is a list of arrays per class
            class_shap = shap_values[prediction][0]
        else:
            # Single array
            class_shap = shap_values[0]

        # Build feature -> SHAP value mapping
        shap_dict = {}
        for i, fname in enumerate(feature_names):
            shap_dict[fname] = round(float(class_shap[i]), 4)

        result["shap_values"] = shap_dict

        # Generate human-readable top factors
        sorted_features = sorted(shap_dict.items(), key=lambda x: abs(x[1]), reverse=True)

        for fname, val in sorted_features[:3]:
            direction = "increases" if val > 0 else "decreases"
            result["top_factors"].append(
                f"{fname} {direction} burnout risk (impact: {abs(val):.4f})"
            )

        result["available"] = True

    except Exception as e:
        result["top_factors"] = [f"SHAP computation error: {str(e)}"]

    return result
