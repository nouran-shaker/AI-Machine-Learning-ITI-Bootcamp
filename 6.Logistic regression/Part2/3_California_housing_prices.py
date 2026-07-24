import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor

cali = fetch_california_housing(as_frame=True)
X = cali.data
y = cali.target

X['RoomsPerPerson'] = X['AveRooms'] / X['Population']

cap_value = np.percentile(X['MedInc'], 97)
X['MedInc'] = np.where(X['MedInc'] > cap_value, cap_value, X['MedInc'])

model = LinearRegression().fit(X, y)

vif_data = pd.DataFrame()
vif_data["Feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
print("Variance Inflation Factor (VIF):")
print(vif_data.sort_values(by="VIF", ascending=False).head())

importance = pd.Series(model.coef_, index=X.columns).sort_values()
importance.plot(kind='barh', color='teal', title='Feature Importance (Coefficients)')
plt.show()

input_data = pd.DataFrame([[4.0, 20.0, 5.0, 1.09, 1200.0, 2.5, 35.6, -119.5, (5.0/1200.0)]], columns=X.columns)
prediction = model.predict(input_data)
print(f"\nPredicted House Price: ${prediction[0] * 100000:,.2f}")