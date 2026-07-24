import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

diabetes = load_diabetes(as_frame=True)
X = diabetes.data
y = diabetes.target

X_interaction = X.copy()
X_interaction['bmi_bp_interaction'] = X_interaction['bmi'] * X_interaction['bp']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_int, X_test_int, _, _ = train_test_split(X_interaction, y, test_size=0.2, random_state=42)

model_base = LinearRegression().fit(X_train, y_train)
model_int = LinearRegression().fit(X_train_int, y_train)

r2_base = r2_score(y_test, model_base.predict(X_test))
r2_int = r2_score(y_test, model_int.predict(X_test_int))

print(f"Base Model R-squared: {r2_base:.4f}")
print(f"Interaction Model R-squared: {r2_int:.4f}")

residuals = y_test - model_int.predict(X_test_int)

plt.scatter(model_int.predict(X_test_int), residuals, color='blue', alpha=0.6)
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residuals vs. Predictions (Interaction Model)')
plt.xlabel('Predicted Progression')
plt.ylabel('Residuals')
plt.show()