import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['Species'] = [species_map[target] for target in iris.target]

print("Observations of each species:", df['Species'].value_counts())