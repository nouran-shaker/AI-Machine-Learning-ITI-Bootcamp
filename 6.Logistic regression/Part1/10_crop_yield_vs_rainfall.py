import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)
rainfall = np.random.uniform(300, 900, 50).reshape(-1, 1)
crop_yield = 2 + 0.007 * rainfall + np.random.normal(0, 0.5, 50).reshape(-1, 1)

model_10 = LinearRegression()
model_10.fit(rainfall, crop_yield)
yield_preds = model_10.predict(rainfall)
residuals_10 = crop_yield - yield_preds

print(f"Predicted yield for 600mm rain: {model_10.predict([[600]])[0][0]:.2f} tons/hectare")

plt.scatter(yield_preds, residuals_10, color='purple')
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Residuals vs. Predictions (Crop Yield)')
plt.xlabel('Predicted Yield')
plt.ylabel('Residuals (Error)')
plt.show()