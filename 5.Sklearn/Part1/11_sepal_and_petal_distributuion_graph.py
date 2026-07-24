import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load data
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])

# Histogram for all measurement columns
df.hist(figsize=(10, 8), bins=20, color='purple')
plt.suptitle("Distribution of Measurements")
plt.tight_layout()
plt.show()