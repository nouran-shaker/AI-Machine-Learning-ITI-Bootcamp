import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

df_modified = df.drop('Id', axis=1, errors='ignore')

print("Modified Dataframe:", df_modified.head())