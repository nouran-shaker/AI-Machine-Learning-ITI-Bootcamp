import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

wine = load_wine()
X = wine.data

std_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()
robust_scaler = RobustScaler()

X_std = std_scaler.fit_transform(X)
X_minmax = minmax_scaler.fit_transform(X)
X_robust = robust_scaler.fit_transform(X)

print("--- Comparison of Row 0 (First 4 Features) ---")
print("1. Original Data:", X[0, :4])
print("2. StandardScaler:", X_std[0, :4])
print("3. MinMaxScaler:  ",X_minmax[0, :4])
print("4. RobustScaler: ", X_robust[0, :4])

print("--- Standard Deviation of Feature 0 ---")
print("Original Std Dev: ",X[:, 0].std())
print("StandardScaler Std Dev: ",X_std[:, 0].std())

fig, axes = plt.subplots(1, 4, figsize=(15, 4))
axes[0].hist(X[:, 0], bins=20, color='gray'); axes[0].set_title('Original')
axes[1].hist(X_std[:, 0], bins=20, color='blue'); axes[1].set_title('StandardScaler')
axes[2].hist(X_minmax[:, 0], bins=20, color='green'); axes[2].set_title('MinMaxScaler')
axes[3].hist(X_robust[:, 0], bins=20, color='red'); axes[3].set_title('RobustScaler')
plt.tight_layout()
plt.show()

pipe = Pipeline([('scaler', StandardScaler()), ('pca', PCA(n_components=2))])
X_pca = pipe.fit_transform(X)