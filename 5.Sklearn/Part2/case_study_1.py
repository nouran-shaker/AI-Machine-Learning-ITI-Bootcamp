import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.impute import SimpleImputer, KNNImputer

iris = load_iris()
X = iris.data.copy()

X[::10] = np.nan

imputer_mean = SimpleImputer(strategy='mean')
imputer_median = SimpleImputer(strategy='median')
imputer_mode = SimpleImputer(strategy='most_frequent')

X_mean = imputer_mean.fit_transform(X)
X_median = imputer_median.fit_transform(X)
X_mode = imputer_mode.fit_transform(X)

total_values = X.size
missing_values = np.isnan(X).sum()
percent_changed = (missing_values / total_values) * 100
print("Percentage of values changed:", percent_changed)


print("--- Comparison of Imputation Strategies on Row 10 ---")
print("1. Original Row 10 (with NaNs): ", X[10])
print("2. Mean Imputed Row 10:   " , X_mean[10])
print("3. Median Imputed Row 10:  ",X_median[10])
print("4. Mode Imputed Row 10:     ",X_mode[10])