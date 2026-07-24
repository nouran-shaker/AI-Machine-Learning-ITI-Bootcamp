# NumPy program to compute pearson product-moment correlation coefficients of two given arrays
import numpy as np

arr1 = np.array([0, 1, 3])
arr2 = np.array([2, 4, 5])

print("Pearson product-moment correlation coefficients of the said arrays:")
print(np.corrcoef(arr1, arr2))