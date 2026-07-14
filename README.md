# 📊 Customer Churn Prediction

## 📌 Overview

Customer Churn Prediction is a Machine Learning classification project that predicts whether a customer is likely to leave a telecom company based on customer demographics, account information, and subscribed services.

The project includes data preprocessing, exploratory data analysis (EDA), feature encoding, model training, evaluation, and prediction using machine learning algorithms.

---

## 🚀 Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Encoding using Label Encoding
- Multiple Machine Learning Models
- Model Comparison
- Customer Churn Prediction
- Model Saving using Joblib

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📂 Project Structure

```
Customer-Churn-Prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── models/
│   └── customer_churn_model.pkl
│
├── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset Information

- **Dataset:** Telco Customer Churn Dataset
- **Total Records:** 7,043
- **Features:** 21
- **Target Variable:** Churn

---

## 🔄 Project Workflow

1. Import Libraries
2. Load Dataset
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Feature Encoding
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Save Best Model
10. Predict Customer Churn

---

## 🤖 Machine Learning Models Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

---

## 📈 Model Performance

| Model | Accuracy |
|--------|---------:|
| Logistic Regression | **78.75%** |
| Decision Tree | **72.49%** |
| Random Forest | **79.25%** ✅ |

**Best Model:** Random Forest Classifier

---

## 📋 Evaluation Metrics

The models were evaluated using:

- Accuracy Score
- Confusion Matrix
- Precision
- Recall
- F1-Score

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Dharanikumar01/Customer-Churn-Prediction.git
```

Move into the project directory:

```bash
cd Customer-Churn-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Train the model:

```bash
cd src
python train.py
```

Predict customer churn:

```bash
python predict.py
```

## 🔮 Future Improvements

- One-Hot Encoding for categorical features
- Hyperparameter Tuning
- Cross Validation
- XGBoost Classifier
- LightGBM Classifier
- Model Deployment using Streamlit or Flask

---

## 👨‍💻 Author

**Dharani Kumar**

- GitHub: https://github.com/Dharanikumar01

---

## ⭐ If you found this project helpful, consider giving it a star!