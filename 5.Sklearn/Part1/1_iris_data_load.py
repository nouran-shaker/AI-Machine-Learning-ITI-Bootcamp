import pandas as pd
from sklearn.datasets import load_iris

# Load data and create dataframe
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

print("Shape of the data:", df.shape)
print("Type of the data:", type(df))
print("First 3 rows:\n", df.head(3))