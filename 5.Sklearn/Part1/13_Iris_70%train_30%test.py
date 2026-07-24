import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

X = df
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

print("--- Training Data (First 5 Rows) ---")
print(X_train.head())

print("--- Testing Data (First 5 Rows) ---")
print(X_test.head())