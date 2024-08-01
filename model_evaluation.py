import pickle
from sklearn.metrics import mean_squared_error, r2_score

# Load the model
with open('nutrition_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')
