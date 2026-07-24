import numpy as np
from sklearn.linear_model import LinearRegression


np.random.seed(42)
house_size = np.random.uniform(1000, 5000, 100).reshape(-1, 1)

price = 50000 + 80 * house_size + np.random.normal(0, 20000, 100).reshape(-1, 1)


model_1 = LinearRegression()
model_1.fit(house_size, price)


prediction_3200 = model_1.predict([[3200]])
print(f"Predicted Price for 3,200 sq ft: ${prediction_3200[0][0]:,.2f}")
print(f"Slope (w): {model_1.coef_[0][0]:.2f}")
print(f"Intercept (b): {model_1.intercept_[0]:.2f}")