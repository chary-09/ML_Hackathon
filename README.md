⚡ Adaptive Burnout Prediction System (ABPS)
Machine Learning • Explainable AI • Student Wellness • Decision Support

An advanced end-to-end machine learning system that predicts student burnout risk,
explains every prediction, and transforms raw outputs into practical academic support.

🌟 Overview
The Adaptive Burnout Prediction System (ABPS) is designed to go far beyond ordinary prediction.

Instead of stopping at a simple burnout classification, this system combines:

📊 multi-model machine learning
🧠 explainable AI with SHAP
💡 insight generation
🩺 recommendation logic
🗓️ daily academic planning
🔮 what-if simulation
🌐 interactive Flask interface
This makes the project feel closer to an intelligent academic support platform than a typical mini-project.

🚀 Key Features
🤖 Multi-Model Prediction Engine
The system trains and evaluates multiple machine learning models for student burnout classification:

Random Forest
Gradient Boosting
Logistic Regression
It compares their performance and automatically identifies the strongest model for prediction.

🧠 Explainable AI Layer
ABPS integrates SHAP-based explainability to reveal the exact features influencing each prediction.

Instead of acting like a black box, the system can explain why a student is predicted as:

Low
Medium
High
burnout risk.

💡 Intelligent Decision Support
The system does not just predict burnout. It also generates:

personalized insights
practical recommendations
student-type classification
performance interpretation
daily planning suggestions
🔮 What-If Simulation Engine
Users can explore how behavioral improvements may reduce burnout risk, such as:

better attendance
balanced study hours
lower assignment delay
higher LMS engagement
stronger academic performance
🌐 Interactive Web Interface
The project includes a Flask-based frontend with:

structured input handling
live prediction output
recommendation display
simulation feedback
explainability-ready integration
📂 Project Architecture
Adaptive_Burnout_Prediction_System/
├── Task_1_Data_Preprocessing/             # 📁 Datasets, utilities, and project notes
├── Task_2_Model_Development/              # 🧪 Training, evaluation, and model selection
├── Task_3_Explainable_Selection/          # 🔍 Explainability, simulation, recommendation, UI
├── Execute_Pipeline.py                    # ▶️ Main Flask application runner
├── Rigorous_Audit_Test.py                 # ✅ Dataset-wise audit and model evaluation
├── requirements.txt                       # 📦 Python dependencies
└── README.md                              # 📘 Project documentation
🧠 Methodology Overview
The goal of this project is not only to classify student burnout, but to do so in a structured, interpretable, and useful way.

The system follows a complete pipeline:

📥 loads burnout-related student datasets
🏷️ separates features and target labels
🔄 encodes categorical burnout levels
✂️ performs train/test splitting
⚙️ applies scaling where required
🤖 trains multiple ML models
📈 compares performance metrics
🏆 selects the best-performing model
🔍 explains predictions using SHAP
💬 transforms results into insights and recommendations
🗓️ generates daily planning suggestions
🔮 simulates improvement scenarios
This layered design helps turn raw machine learning output into a practical support system.

📊 Core Inputs
The prediction engine uses the following academic and behavioral indicators:

attendance
study hours
assignment delay
LMS usage
academic performance
These features collectively help estimate a student’s burnout intensity.

🎯 System Outputs
For each prediction cycle, the system can generate:

burnout level prediction
class probability distribution
burnout score
best-model information
model comparison metrics
feature importance output
SHAP explanation factors
insight summary
practical recommendations
student type classification
daily academic plan
improvement simulation scenarios
🛠️ Tech Stack
🐍 Python
🌐 Flask
🐼 Pandas
🔢 NumPy
🤖 Scikit-learn
🔍 SHAP
🎨 HTML
🎨 CSS
⚡ JavaScript
🔍 Task-Wise Breakdown
📁 Task 1: Data Preprocessing
Includes:

datasets
helper utilities
supporting constants
project notes and documentation
🧪 Task 2: Model Development
Includes:

model training logic
model comparison
evaluation metrics
best-model selection
audit-ready testing scripts
🔍 Task 3: Explainable Selection
Includes:

SHAP explainability engine
recommendation engine
insight engine
planner engine
performance engine
adaptive logging engine
simulation engine
frontend templates and static assets
▶️ Installation & Usage
1. Install dependencies
pip install -r requirements.txt
2. Run the main application
python Execute_Pipeline.py
3. Run the audit script
python Rigorous_Audit_Test.py
🌍 Project Vision
This project is built around one important belief:

Student burnout prediction should not stop at classification.
It should also explain risk, guide intervention, and help improve outcomes.

That is why ABPS combines machine learning, explainability, recommendations, and simulation into one integrated workflow.

✨ Final Impression
If someone opens this repository expecting a small student project, they will instead discover a structured, explainable, and application-ready machine learning system with real depth across modeling, interpretability, and usability.

👨‍💻 Author
Built as a complete machine learning project focused on:

prediction quality
model transparency
practical academic support
clean task-wise repository structure
