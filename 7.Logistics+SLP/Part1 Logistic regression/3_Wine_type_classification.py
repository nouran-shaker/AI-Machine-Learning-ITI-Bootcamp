import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

wine = load_wine(as_frame=True)
X = wine.data
y = wine.target

binary_mask = y < 2
X_bin = X[binary_mask]
y_bin = y[binary_mask]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_bin)

model_sag = LogisticRegression(solver='sag', max_iter=5000, random_state=42)
model_sag.fit(X_scaled, y_bin)

model_lbfgs = LogisticRegression(solver='lbfgs', max_iter=5000, random_state=42)
model_lbfgs.fit(X_scaled, y_bin)

print(f"SAG Solver Iterations to Converge: {model_sag.n_iter_[0]}")
print(f"LBFGS Solver Iterations to Converge: {model_lbfgs.n_iter_[0]}")

cv_scores = cross_val_score(model_sag, X_scaled, y_bin, cv=5)
print(f"\n5-Fold CV Mean Accuracy: {cv_scores.mean():.4f}")

feature_importance = pd.Series(model_sag.coef_[0], index=X.columns).sort_values()

plt.figure(figsize=(10, 6))
feature_importance.plot(kind='barh', color='darkred')
plt.title('Feature Importance (Logistic Regression - Wine Binary)')
plt.xlabel('Coefficient Value')
plt.show()