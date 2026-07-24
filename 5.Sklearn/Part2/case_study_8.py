import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


digits = load_digits()
X, y = digits.data, digits.target

rfc = RandomForestClassifier(random_state=42)
rfecv = RFECV(estimator=rfc, step=1, cv=StratifiedKFold(3), scoring='accuracy')
rfecv.fit(X, y)

print("--- Feature Selection Results ---")
print("Original number of pixels: ",X.shape[1])
print("Optimal number of pixels:  ",rfecv.n_features_)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(range(1, len(rfecv.cv_results_['mean_test_score']) + 1), rfecv.cv_results_['mean_test_score'])
plt.title("Accuracy vs. Number of Features")
plt.xlabel("Number of Pixels Selected")
plt.ylabel("Cross-Validation Accuracy")

plt.subplot(1, 2, 2)

pixel_ranks = rfecv.ranking_.reshape(8, 8)
plt.imshow(pixel_ranks, cmap='hot_r')
plt.colorbar(label='Feature Rank (1 = Best)')
plt.title("Pixel Importance Heatmap")

plt.tight_layout()
plt.show()