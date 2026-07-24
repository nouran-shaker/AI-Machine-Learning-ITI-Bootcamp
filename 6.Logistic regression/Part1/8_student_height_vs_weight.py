import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

np.random.seed(42)
height = np.random.uniform(150, 200, 100).reshape(-1, 1)
weight = 0.8 * height - 70 + np.random.normal(0, 5, 100).reshape(-1, 1) 

model_8 = LinearRegression()
model_8.fit(height, weight)
weight_pred = model_8.predict(height)
mse_8 = mean_squared_error(weight, weight_pred)

print(f"MSE: {mse_8:.2f}")
print(f"Intercept: {model_8.intercept_[0]:.2f}")
print(f"Predicted weight for 175cm: {model_8.predict([[175]])[0][0]:.2f} kg")