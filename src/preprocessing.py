import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    # Convert TotalCharges to numeric
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df.dropna(inplace=True)

    # Drop customer ID
    df = df.drop("customerID", axis=1)

    # Encode categorical columns
    le = LabelEncoder()

    for col in df.select_dtypes(include="object").columns:
        df[col] = le.fit_transform(df[col])

    return df