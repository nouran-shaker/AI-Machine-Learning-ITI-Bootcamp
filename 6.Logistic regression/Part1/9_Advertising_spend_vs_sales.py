import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

np.random.seed(42)
tv_budget = np.random.uniform(1, 100, 100).reshape(-1, 1)
sales_ad = 50 + 8 * tv_budget + np.random.normal(0, 30, 100).reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(tv_budget, sales_ad, test_size=0.25, random_state=42)

model_9 = LinearRegression()
model_9.fit(X_train, y_train)

print(f"Sales increase per $1k spent: {model_9.coef_[0][0]:.2f} units")
print(f"Predicted sales for $80k budget: {model_9.predict([[80]])[0][0]:.2f} units")