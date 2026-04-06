from flask import Flask, render_template, request
import pandas as pd

from Task_2_Model_Development.model import (
    predict_burnout,
    get_model_metrics,
    get_best_model,
    get_feature_importance,
    get_full_metrics,
    X,
    X_train,
    best_model,
    best_model_name,
)
from Task_3_Explainable_Selection.engine.insight_engine import generate_insights
from Task_3_Explainable_Selection.engine.recommendation_engine import generate_recommendations
from Task_3_Explainable_Selection.engine.performance_engine import analyze_performance, classify_student
from Task_3_Explainable_Selection.engine.adaptive_engine import save_log, load_logs
from Task_3_Explainable_Selection.engine.simulation_engine import run_simulation
from Task_3_Explainable_Selection.engine.planner_engine import generate_daily_plan
from Task_3_Explainable_Selection.engine.explainability_engine import explain_prediction

app = Flask(
    __name__,
    template_folder="Task_3_Explainable_Selection/templates",
    static_folder="Task_3_Explainable_Selection/static",
)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    probabilities = {}
    burnout_score = 0
    message = ""

    insights = []
    recommendations = []
    performance_msg = ""
    student_type = ""
    daily_plan = []
    simulation_results = []
    shap_result = {"top_factors": [], "shap_values": {}, "available": False}
    input_data = {}

    history = load_logs()

    metrics = get_model_metrics()
    best_model_info = get_best_model()
    feature_importance = get_feature_importance()
    full_metrics = get_full_metrics()

    if request.method == "POST":
        data = [
            float(request.form["attendance"]),
            float(request.form["study_hours"]),
            float(request.form["assignment_delay"]),
            float(request.form["lms_usage"]),
            float(request.form["performance"]),
        ]

        prediction, probabilities, burnout_score, message = predict_burnout(data)

        data_dict = {
            "attendance": data[0],
            "study_hours": data[1],
            "assignment_delay": data[2],
            "lms_usage": data[3],
            "performance": data[4],
        }

        input_data = data_dict

        insights = generate_insights(data_dict)
        recommendations = generate_recommendations(insights, burnout_score)
        performance_msg = analyze_performance(data[4], prediction)
        student_type = classify_student(data[4], prediction)
        daily_plan = generate_daily_plan(data_dict, burnout_score)
        simulation_results = run_simulation(data_dict, predict_burnout, burnout_score)

        try:
            shap_result = explain_prediction(
                model=best_model,
                model_name=best_model_name,
                data_df=pd.DataFrame([data], columns=X.columns),
                feature_names=list(X.columns),
                X_train=X_train,
            )
        except Exception:
            shap_result = {
                "top_factors": ["Explainability not available"],
                "shap_values": {},
                "available": False,
            }

        save_log(data_dict, prediction, burnout_score)
        history = load_logs()

    return render_template(
        "index.html",
        prediction=prediction,
        probabilities=probabilities,
        burnout_score=burnout_score,
        message=message,
        insights=insights,
        recommendations=recommendations,
        performance_msg=performance_msg,
        student_type=student_type,
        daily_plan=daily_plan,
        simulation_results=simulation_results,
        shap_result=shap_result,
        input_data=input_data,
        history=history,
        metrics=metrics,
        best_model=best_model_info,
        feature_importance=feature_importance,
        full_metrics=full_metrics,
    )


if __name__ == "__main__":
    app.run(debug=True)
