import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

print("Number of observations:", len(df))
print("Missing values per column:", df.isnull().sum())
print("Total NaN values:", df.isnull().sum().sum())