import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

first_four_cells = df.iloc[0, 0:4]

print("First four cells of row 0:", first_four_cells)