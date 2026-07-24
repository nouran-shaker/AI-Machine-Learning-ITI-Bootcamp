import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error

housing = fetch_california_housing(as_frame=True)
df = housing.frame.dropna().drop_duplicates() # Clean missing/dupes
X, y = df.drop('MedHouseVal', axis=1), df['MedHouseVal']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_model = LinearRegression().fit(X_train, y_train)
dt_model = DecisionTreeRegressor(max_depth=5, random_state=42).fit(X_train, y_train)

lr_preds = lr_model.predict(X_test)
dt_preds = dt_model.predict(X_test)


def print_metrics(name, y_true, y_pred):
    print(name," Metrics")
    print("MAE:",  mean_absolute_error(y_true, y_pred))
    print("MSE: ",mean_squared_error(y_true, y_pred))
    print("RMSE: ",np.sqrt(mean_squared_error(y_true, y_pred)))
    print("R^2: ",r2_score(y_true, y_pred))
    print("MAPE: ",mean_absolute_percentage_error(y_true, y_pred))

print_metrics("Linear Regression", y_test, lr_preds)
print_metrics("Decision Tree", y_test, dt_preds)

residuals = y_test - lr_preds
plt.figure(figsize=(8, 5))
plt.scatter(lr_preds, residuals, alpha=0.3, color='purple')
plt.axhline(y=0, color='red', linestyle='--')
plt.title("Residuals vs. Predicted Values (Linear Regression)")
plt.xlabel("Predicted House Value")
plt.ylabel("Residual (Actual - Predicted)")
plt.show()