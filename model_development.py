import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Load data from the database
def load_data():
    conn = sqlite3.connect('nutrition.db')
    df = pd.read_sql_query("SELECT * FROM user_data", conn)
    conn.close()
    return df

# Preprocess data
def preprocess_data(df):
    X = df[['age', 'weight', 'height', 'daily_caloric_intake']]
    y = df[['recommended_caloric_intake']]
    X = pd.get_dummies(X, columns=['dietary_preferences', 'health_conditions'])
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
def train_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train.values.ravel())
    return model

df = load_data()
X_train, X_test, y_train, y_test = preprocess_data(df)
model = train_model(X_train, y_train)

# Save the model
import pickle
with open('nutrition_model.pkl', 'wb') as file:
    pickle.dump(model, file)
