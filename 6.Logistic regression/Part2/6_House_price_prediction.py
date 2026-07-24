import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import r2_score

data = pd.DataFrame({
    'YearBuilt': [2000, np.nan, 1950, 2010, 1980],
    'Neighborhood': ['CollgCr', 'Veenker', np.nan, 'NoRidge', 'CollgCr'],
    'LotArea': [8450, 9600, 11250, 14260, 14115],
    'SalePrice': [208500, 181500, 223500, 250000, 143000]
})

numeric_cols = ['YearBuilt', 'LotArea']
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

categorical_cols = ['Neighborhood']
data[categorical_cols] = data[categorical_cols].fillna(data[categorical_cols].mode().iloc[0])

data['HouseAge'] = 2023 - data['YearBuilt']

data_encoded = pd.get_dummies(data, columns=['Neighborhood'])

X = data_encoded.drop(['SalePrice', 'YearBuilt'], axis=1)
y = data_encoded['SalePrice']

ols_model = LinearRegression().fit(X, y)
ridge_model = Ridge(alpha=1.0).fit(X, y)

print(f"OLS R-squared: {r2_score(y, ols_model.predict(X)):.4f}")
print(f"Ridge R-squared: {r2_score(y, ridge_model.predict(X)):.4f}")

neighborhood_coeffs = {col: coef for col, coef in zip(X.columns, ridge_model.coef_) if 'Neighborhood' in col}
most_valuable = max(neighborhood_coeffs, key=neighborhood_coeffs.get)
print(f"Most valuable neighborhood feature: {most_valuable}")