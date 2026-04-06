# Adaptive Burnout Prediction System

This repository is organized into task-wise folders so it looks clean and professional on GitHub.

## Project Structure

- `Task_1_Data_Preprocessing/` contains datasets, utility files, and project notes used for data preparation.
- `Task_2_Model_Development/` contains model training, model comparison, and evaluation code.
- `Task_3_Explainable_Selection/` contains explainability, recommendations, simulation, logs, and the Flask UI assets.
- `Execute_Pipeline.py` is the main entry point for running the web application.
- `Rigorous_Audit_Test.py` runs dataset-wise model audits for validation.
- `requirements.txt` lists the Python dependencies needed for the project.

## How To Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the web app:

```bash
python Execute_Pipeline.py
```

Run the audit script:

```bash
python Rigorous_Audit_Test.py
```

## Main Features

- Student burnout level prediction using machine learning models
- Model comparison using accuracy, precision, recall, F1-score, and ROC-AUC
- Explainable AI support using SHAP
- Personalized insights, recommendations, daily plan generation, and what-if simulation
- Flask-based interface for interactive testing
