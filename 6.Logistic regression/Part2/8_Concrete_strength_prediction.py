import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor

data = pd.DataFrame({
    'Water': [162, 162, 228, 228, 192],
    'Cement': [540, 540, 332, 332, 198],
    'Strength': [79.99, 61.89, 40.27, 41.05, 44.30]
})

data['Water_Cement_Ratio'] = data['Water'] / data['Cement']

X = data[['Water', 'Cement', 'Water_Cement_Ratio']]
y = data['Strength']

vif_data = pd.DataFrame()
vif_data["Feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]
print(vif_data)
print("-" * 30)

model_simple = LinearRegression().fit(X, y)
r2_simple = r2_score(y, model_simple.predict(X))

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model_poly = LinearRegression().fit(X_poly, y)
r2_poly = r2_score(y, model_poly.predict(X_poly))

print(f"Simple Linear R-squared: {r2_simple:.4f}")
print(f"Polynomial (Degree 2) R-squared: {r2_poly:.4f}")