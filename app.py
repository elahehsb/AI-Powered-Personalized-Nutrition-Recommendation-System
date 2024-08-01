from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the model and scaler
with open('nutrition_model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    df = pd.get_dummies(df, columns=['dietary_preferences', 'health_conditions'])
    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    
    prediction = model.predict(df)
    return jsonify({'recommended_caloric_intake': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
