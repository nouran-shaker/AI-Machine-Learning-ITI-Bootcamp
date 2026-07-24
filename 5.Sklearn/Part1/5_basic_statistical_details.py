import pandas as pd
from sklearn.datasets import load_iris

# Load data
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

print("Basic statistical details:", df.describe())