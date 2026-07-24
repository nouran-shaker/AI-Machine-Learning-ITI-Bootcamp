import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.linear_model import LogisticRegression


iris = load_iris()
X, y = iris.data.copy(), iris.target
np.random.seed(42)
X[np.random.choice(X.shape[0], 20, replace=False), 0] = np.nan # Add NaNs to col 0

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


pipe_pca = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('pca', PCA(n_components=2)),
    ('classifier', LogisticRegression())
])


pipe_poly = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('poly', PolynomialFeatures(degree=2)),
    ('selector', SelectKBest(k=5)),
    ('classifier', LogisticRegression(max_iter=1000))
])

pipe_pca.fit(X_train, y_train)
pipe_poly.fit(X_train, y_train)

print("--- Pipeline Accuracy Comparison ---")
print("Pipeline 1 (PCA) Accuracy: ",pipe_pca.score(X_test, y_test))
print("Pipeline 2 (Poly) Accuracy: ",pipe_poly.score(X_test, y_test))

X_train_pca = pipe_pca.named_steps['pca'].transform(
    pipe_pca.named_steps['scaler'].transform(
        pipe_pca.named_steps['imputer'].transform(X_train)
    )
)

plt.figure(figsize=(8, 5))
scatter = plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1], c=y_train, cmap='viridis', edgecolor='k')
plt.title("Data Transformed by Pipeline (PCA step)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend(handles=scatter.legend_elements()[0], labels=iris.target_names.tolist())
plt.show()