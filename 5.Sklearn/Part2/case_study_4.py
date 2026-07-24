from sklearn.datasets import load_diabetes
from sklearn.feature_selection import SelectKBest, mutual_info_regression, f_regression, RFE
from sklearn.linear_model import LinearRegression

data = load_diabetes()
X, y = data.data, data.target
feature_names = data.feature_names

selector_mi = SelectKBest(score_func=mutual_info_regression, k=5)
X_mi = selector_mi.fit_transform(X, y)

selector_f = SelectKBest(score_func=f_regression, k=5)
X_f = selector_f.fit_transform(X, y)

estimator = LinearRegression()
rfe = RFE(estimator, n_features_to_select=5)
X_rfe = rfe.fit_transform(X, y)


print("--- Dataset Shape Reduction ---")
print("Original dataset shape:", X.shape," (10 Features)")
print("Reduced dataset shape: ", X_mi.shape," (5 Features)")

print("--- Features Selected by Method ---")
print("1. Mutual Info:", [feature_names[i] for i in selector_mi.get_support(indices=True)])
print("2. f-regression:", [feature_names[i] for i in selector_f.get_support(indices=True)])
print("3. RFE:         ", [feature_names[i] for i, selected in enumerate(rfe.support_) if selected])