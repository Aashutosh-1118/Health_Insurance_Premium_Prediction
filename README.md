# 🏥 Health Insurance Premium Prediction

This is a **Machine Learning–based web application** that predicts the **health insurance premium cost** based on user details such as age, income, BMI category, smoking status, medical history, insurance plan, and number of dependents.

🔗 **Live App:** [health-insurance-premium-prediction1.streamlit.app](https://health-insurance-premium-prediction1.streamlit.app/)


---

## 🧠 Model Strategy (Age-Based)

The prediction pipeline is designed using **two different machine learning models**:

- **Users with age <= 25**
  - Model used: **Linear Regression**
  - Reason: Premium patterns are simpler and more linear for younger individuals

- **Users with age > 25**
  - Model used: **XGBoost Regressor**
  - Reason: Premium calculations become more complex due to higher health risks and non-linear factors

The appropriate model is selected **dynamically at runtime** based on the user's age.

---

---
## 📊 Model Evaluation

Initially trained a single model on the full dataset — looked strong overall (R² ≈ 0.98),
but error analysis showed ~30% of predictions had >10% error, concentrated in users aged 25 and under.

Splitting by age alone didn't fix it — the young-user model actually got worse in isolation (R² dropped to ~0.56),
since that segment had less behavioral/medical signal to work with.

Adding a missing `genetical_risk` feature for the young segment fixed this:

| Segment | Model | R² (test) |
|---|---|---|
| Age ≤ 25 | Linear Regression | 0.989 |
| Age > 25 | XGBoost | 0.998 |

Linear Regression outperformed XGBoost on the young segment — likely overfitting on a smaller,
lower-signal dataset. That's why the deployed app uses Linear Regression for younger users
and XGBoost for everyone else.

---


## 📁 Project Structure

```text
Health_Insurance_Premium_Prediction/
│
├── artifacts/
│   ├── model_young.joblib       # Trained model for age <= 25 (Linear Regression)
│   ├── model_rest.joblib        # Trained model for age > 25 (XGBoost Regressor)
│   ├── scaler_young.joblib      # Feature scaler for age <= 25
│   └── scaler_rest.joblib       # Feature scaler for age > 25
│
├── main.py                      # Application entry point (Streamlit UI)
├── prediction_helper.py         # Model loading & prediction logic
│
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
├── LICENSE                      # Apache 2.0 License
└── .gitignore
```

## ⚙️ Tech Stack

- **Programming Language:** Python  
- **Machine Learning:** Linear Regression, XGBoost, Scikit-learn  
- **Web Framework:** Streamlit  
- **Model Persistence:** Joblib  

---

## 🚀 How to Run the Project

```bash
# Clone repository
git clone https://github.com/Aashutosh-1118/Health_Insurance_Premium_Prediction.git

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run main.py

