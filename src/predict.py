import pandas as pd
import joblib

# Load trained model
model = joblib.load("../models/customer_churn_model.pkl")

# Sample customer
sample = pd.DataFrame({
    "gender": [0],
    "SeniorCitizen": [0],
    "Partner": [1],
    "Dependents": [0],
    "tenure": [24],
    "PhoneService": [1],
    "MultipleLines": [0],
    "InternetService": [1],
    "OnlineSecurity": [1],
    "OnlineBackup": [0],
    "DeviceProtection": [1],
    "TechSupport": [1],
    "StreamingTV": [0],
    "StreamingMovies": [0],
    "Contract": [1],
    "PaperlessBilling": [1],
    "PaymentMethod": [2],
    "MonthlyCharges": [70.5],
    "TotalCharges": [1700.5]
})

prediction = model.predict(sample)

print("Prediction:", "Customer will Churn" if prediction[0] == 1 else "Customer will Stay")