import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score, roc_curve

data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target

print("Class Balance:\n", y.value_counts(normalize=True))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_none = LogisticRegression(penalty=None, max_iter=10000)
model_none.fit(X_train, y_train)
y_pred = model_none.predict(X_test)
y_proba = model_none.predict_proba(X_test)[:, 1]

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print(f"ROC-AUC Score: {roc_auc_score(y_test, y_proba):.4f}")

param_grid = {'C': [0.01, 0.1, 1, 10, 100]}
grid_search = GridSearchCV(LogisticRegression(penalty='l2', max_iter=10000), param_grid, cv=5)
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
print(f"\nBest C value for L2 Regularization: {grid_search.best_params_['C']}")

coefficients = pd.Series(best_model.coef_[0], index=X.columns)
top_3_features = coefficients.abs().sort_values(ascending=False).head(3)
print("\nTop 3 Most Important Features (L2 Model):")
print(top_3_features)