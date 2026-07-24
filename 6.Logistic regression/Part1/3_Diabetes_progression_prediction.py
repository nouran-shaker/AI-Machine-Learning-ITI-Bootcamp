import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
import numpy as np 

diabetes = load_diabetes()
X_bmi = diabetes.data[:, np.newaxis, 2] # Extracting just the BMI column
y_progression = diabetes.target

model_3 = LinearRegression()
model_3.fit(X_bmi, y_progression)
y_pred = model_3.predict(X_bmi)

plt.scatter(X_bmi, y_progression, color='blue', alpha=0.5, label='Actual Data')
plt.plot(X_bmi, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('BMI (Scaled)')
plt.ylabel('Disease Progression')
plt.legend()
plt.show()

r2 = r2_score(y_progression, y_pred)
print(f"R-squared Score: {r2:.4f}")
print(f"Slope: {model_3.coef_[0]:.2f}")