import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

binary_mask = y < 2
X_binary = X[binary_mask][:, [0, 3]]
y_binary = y[binary_mask]

X_train, X_test, y_train, y_test = train_test_split(X_binary, y_binary, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

print(f"Base Model Accuracy: {accuracy_score(y_test, model.predict(X_test)):.4f}")
print(f"Base Coefficients: Sepal Length = {model.coef_[0][0]:.4f}, Petal Width = {model.coef_[0][1]:.4f}")

w1, w2 = model.coef_[0]
b = model.intercept_[0]
x1_min, x1_max = X_binary[:, 0].min() - 0.5, X_binary[:, 0].max() + 0.5
x2_boundary = -(w1 * np.array([x1_min, x1_max]) + b) / w2

plt.scatter(X_binary[:, 0], X_binary[:, 1], c=y_binary, cmap='bwr', edgecolor='k')
plt.plot([x1_min, x1_max], x2_boundary, color='black', linestyle='--')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')
plt.title('Decision Boundary (Setosa vs Versicolor)')
plt.show()

np.random.seed(42)
dummy_feature = np.random.rand(X_binary.shape[0], 1)
X_noisy = np.hstack((X_binary, dummy_feature))

X_train_n, X_test_n, y_train_n, y_test_n = train_test_split(X_noisy, y_binary, test_size=0.2, random_state=42)
model_noisy = LogisticRegression().fit(X_train_n, y_train_n)

print("\nAfter adding random noise feature:")
print(f"Coefficients: Sepal Length = {model_noisy.coef_[0][0]:.4f}, Petal Width = {model_noisy.coef_[0][1]:.4f}, Noise = {model_noisy.coef_[0][2]:.4f}")