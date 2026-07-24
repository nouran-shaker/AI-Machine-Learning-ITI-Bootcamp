from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np

np.random.seed(42)
experience = np.random.uniform(0, 20, 100).reshape(-1, 1)
salary = 40 + 8 * experience + np.random.normal(0, 10, 100).reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(experience, salary, test_size=0.3, random_state=42)

model_5 = LinearRegression()
model_5.fit(X_train, y_train)

y_pred = model_5.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f"R-squared: {r2:.4f}")
print(f"Predicted salary for 15 years: ${model_5.predict([[15]])[0][0]:.2f}k")