import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(42)
price = np.random.uniform(10, 50, 50).reshape(-1, 1)
demand = 300 - 6 * price + np.random.normal(0, 15, 50).reshape(-1, 1)

model_7 = LinearRegression()
model_7.fit(price, demand)
demand_pred = model_7.predict(price)

residuals = demand - demand_pred

pred_35 = model_7.predict([[35]])
print(f"Slope (w): {model_7.coef_[0][0]:.2f}")
print(f"Predicted demand at $35: {pred_35[0][0]:.0f} units")