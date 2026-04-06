import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score


def eval_dataset(path):
    df = pd.read_csv(path)
    X = df.drop('burnout_level', axis=1)
    y = df['burnout_level']
    y_enc = LabelEncoder().fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_enc, test_size=0.2, stratify=y_enc, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    rf = RandomForestClassifier(n_estimators=300, max_depth=15, min_samples_split=5, random_state=42)
    gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=5)
    lr = LogisticRegression(max_iter=2000)

    rf.fit(X_train, y_train)
    gb.fit(X_train, y_train)
    lr.fit(X_train_scaled, y_train)

    models = {'Random Forest': rf, 'Gradient Boosting': gb, 'Logistic Regression': lr}
    results = {}

    for name, model in models.items():
        if name == 'Logistic Regression':
            pred = model.predict(X_test_scaled)
            pred_proba = model.predict_proba(X_test_scaled)
        else:
            pred = model.predict(X_test)
            pred_proba = model.predict_proba(X_test)
        
        acc = accuracy_score(y_test, pred) * 100
        prec = precision_score(y_test, pred, average='weighted') * 100
        rec = recall_score(y_test, pred, average='weighted') * 100
        f1 = f1_score(y_test, pred, average='weighted') * 100
        auc = roc_auc_score(y_test, pred_proba, multi_class='ovr', average='weighted') * 100
        
        results[name] = {
            'Accuracy': acc,
            'Precision': prec,
            'Recall': rec,
            'F1-Score': f1,
            'ROC-AUC': auc
        }

    return results


if __name__ == '__main__':
    base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    for fname in [
        'indian_student_burnout_dataset_120.csv',
        'student_burnout_dataset_2000_fixed.csv',
        'student_burnout_dataset_5000.csv',
    ]:
        path = os.path.join(base, 'Task_1_Data_Preprocessing', 'data', fname)
        metrics = eval_dataset(path)
        print(f"Dataset: {fname}")
        for model, scores in metrics.items():
            print(f"  {model}:")
            for metric, value in scores.items():
                print(f"    {metric}: {value:.2f}%")
        print()
