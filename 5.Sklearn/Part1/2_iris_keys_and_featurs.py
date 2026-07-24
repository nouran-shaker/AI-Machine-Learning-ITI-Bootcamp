from sklearn.datasets import load_iris

iris = load_iris()

print("Keys:", iris.keys())
print("Number of rows-columns:", iris.data.shape)
print("Feature names:", iris.feature_names)
print("Description:", iris.DESCR)