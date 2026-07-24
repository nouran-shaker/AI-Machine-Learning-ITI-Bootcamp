# NumPy program to compute cross-correlation of two given arrays
import numpy as np

arr1 = np.array([0, 1, 3])
arr2 = np.array([2, 4, 5])

print("Cross-correlation of the said arrays:")
print(np.correlate(arr1, arr2))