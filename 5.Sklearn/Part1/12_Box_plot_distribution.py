import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load data and setup species categories
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])

species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['Species'] = [species_map[target] for target in iris.target]

plt.figure(figsize=(8, 6))
sns.boxplot(x='Species', y='SepalLengthCm', data=df)
plt.title('Distribution of Sepal Length by Species')
plt.show()