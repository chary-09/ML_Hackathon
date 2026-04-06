import pandas as pd
import os

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# -------------------------
# Load Dataset
# -------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
file_path = os.path.join(
    BASE_DIR,
    "Task_1_Data_Preprocessing",
    "data",
    "student_burnout_dataset_5000.csv",
)
# file_path = os.path.join(BASE_DIR, "data", "student_burnout_dataset_2000_fixed.csv")
# file_path = os.path.join(BASE_DIR, "data", "indian_student_burnout_dataset_120.csv")


df = pd.read_csv(file_path)


# -------------------------
# Features and Target
# -------------------------

X = df.drop("burnout_level", axis=1)
y = df["burnout_level"]


# -------------------------
# Encode Labels
# -------------------------

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)


# -------------------------
# Train Test Split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    stratify=y_encoded,
    random_state=42
)


# -------------------------
# Feature Scaling
# -------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# -------------------------
# Models
# -------------------------

rf = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    min_samples_split=5,
    random_state=42
)

gb = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=5
)

lr = LogisticRegression(max_iter=2000)


# -------------------------
# Train Models
# -------------------------

rf.fit(X_train, y_train)
gb.fit(X_train, y_train)
lr.fit(X_train_scaled, y_train)


# -------------------------
# Predictions
# -------------------------

rf_pred = rf.predict(X_test)
gb_pred = gb.predict(X_test)
lr_pred = lr.predict(X_test_scaled)


# -------------------------
# Accuracy
# -------------------------

rf_acc = accuracy_score(y_test, rf_pred)
gb_acc = accuracy_score(y_test, gb_pred)
lr_acc = accuracy_score(y_test, lr_pred)


# -------------------------
# Best Model Selection
# -------------------------

models = {
    "Random Forest": (rf, rf_acc),
    "Gradient Boosting": (gb, gb_acc),
    "Logistic Regression": (lr, lr_acc)
}

best_model_name = max(models, key=lambda x: models[x][1])
best_model = models[best_model_name][0]


# -------------------------
# Advanced Metrics
# -------------------------

precision = precision_score(y_test, rf_pred, average="weighted")
recall = recall_score(y_test, rf_pred, average="weighted")
f1 = f1_score(y_test, rf_pred, average="weighted")



# -------------------------
# Prediction Function
# -------------------------

def predict_burnout(data):

    data_df = pd.DataFrame([data], columns=X.columns)

    data_scaled = scaler.transform(data_df)

    if best_model_name == "Logistic Regression":
        probs = best_model.predict_proba(data_scaled)[0]
    else:
        probs = best_model.predict_proba(data_df)[0]

    labels = encoder.inverse_transform([0, 1, 2])
    prediction = labels[probs.argmax()]

    prob_dict = dict(zip(labels, probs))

    high_score = prob_dict.get("High", 0) * 100
    medium_score = prob_dict.get("Medium", 0) * 100

    burnout_score = round((0.5 * medium_score + high_score), 2)

    if burnout_score < 35:
        message = "Low stress detected."
    elif burnout_score < 65:
        message = "Moderate stress detected."
    else:
        message = "High stress detected."

    return prediction, prob_dict, burnout_score, message


# -------------------------
# Evaluation Metrics
# -------------------------

def get_full_metrics():

    return {
        "Accuracy": round(models[best_model_name][1] * 100, 2),
        "Precision": round(precision * 100, 2),
        "Recall": round(recall * 100, 2),
        "F1 Score": round(f1 * 100, 2)
    }


# -------------------------
# Model Comparison
# -------------------------

def get_model_metrics():

    return {
        "Random Forest": round(rf_acc * 100, 2),
        "Gradient Boosting": round(gb_acc * 100, 2),
        "Logistic Regression": round(lr_acc * 100, 2)
    }


# -------------------------
# Best Model
# -------------------------

def get_best_model():
    return best_model_name


# -------------------------
# Feature Importance
# -------------------------

def get_feature_importance():

    importance = rf.feature_importances_

    return dict(zip(X.columns, importance))
