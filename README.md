# 🏥 Health Insurance Premium Prediction

This is a **Machine Learning–based web application** that predicts the **health insurance premium cost** based on user details such as age, income, BMI category, smoking status, medical history, insurance plan, and number of dependents.

---

## 🧠 Model Strategy (Age-Based)

The prediction pipeline is designed using **two different machine learning models**:

- **Users with age < 25**
  - Model used: **Linear Regression**
  - Reason: Premium patterns are simpler and more linear for younger individuals

- **Users with age ≥ 25**
  - Model used: **XGBoost Regressor**
  - Reason: Premium calculations become more complex due to higher health risks and non-linear factors

The appropriate model is selected **dynamically at runtime** based on the user's age.

---

## 📁 Project Structure

```text
Health_Insurance_Premium_Prediction/
│
├── artifacts/
│   └── model_rest.joblib        # Trained ML model
│
├── main.py                      # Application entry point
├── prediction_helper.py         # Model loading & prediction logic
│
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
├── LICENSE                      # Apache 2.0 License
└── .git


