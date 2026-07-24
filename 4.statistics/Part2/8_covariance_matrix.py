# NumPy program to compute the covariance matrix of two given arrays
import numpy as np

arr1 = np.array([0, 1, 2])
arr2 = np.array([2, 1, 0])

print("Covariance matrix of the said arrays:")
print(np.cov(arr1, arr2))