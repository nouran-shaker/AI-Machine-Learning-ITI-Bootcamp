from sklearn.linear_model import LinearRegression
import numpy as np 

np.random.seed(42)
temperature = np.random.uniform(15, 35, 50).reshape(-1, 1)
sales = 20 + 5 * temperature + np.random.normal(0, 10, 50).reshape(-1, 1)

model_4 = LinearRegression()
model_4.fit(temperature, sales)

pred_25 = model_4.predict([[25]])
print(f"Predicted sales at 25°C: {pred_25[0][0]:.2f} units")
print(f"Intercept (Sales at 0°C): {model_4.intercept_[0]:.2f}")
