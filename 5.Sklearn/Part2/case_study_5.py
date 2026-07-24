import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

boston = fetch_openml(name='boston', version=1, as_frame=True, parser='auto')
df = boston.frame
df_numeric = df.select_dtypes(include=[np.number]).dropna() 
X = df_numeric.drop('MEDV', axis=1)
y = df_numeric['MEDV']

z_scores = np.abs(stats.zscore(X))
z_mask = (z_scores < 3).all(axis=1)
X_z_clean, y_z_clean = X[z_mask], y[z_mask]

iso_forest = IsolationForest(contamination=0.05, random_state=42)
iso_predictions = iso_forest.fit_predict(X)
iso_mask = iso_predictions == 1
X_iso_clean, y_iso_clean = X[iso_mask], y[iso_mask]

print("--- Outlier Removal Summary ---")
print("Original rows:     ",len(X))
print("After Z-Score removal: ",len(X_z_clean)," (Dropped ",len(X) - len(X_z_clean)," rows)")
print("After Isolation Forest: ",len(X_iso_clean)," (Dropped ",len(X) - len(X_iso_clean)," rows)")

print("--- Model Performance (Mean Squared Error) ---")
def test_model(X_data, y_data, title):
    model = LinearRegression().fit(X_data, y_data)
    mse = mean_squared_error(y_data, model.predict(X_data))
    print(f"{title}: {mse:.2f}")

test_model(X, y, "Original Data MSE")
test_model(X_z_clean, y_z_clean, "Z-Score Cleaned MSE")
test_model(X_iso_clean, y_iso_clean, "Iso-Forest Cleaned MSE")

plt.figure(figsize=(10, 5))
sns.boxplot(data=X[['CRIM', 'ZN', 'B']]) 
plt.title("Boxplot for Outlier Visualization")
plt.show()