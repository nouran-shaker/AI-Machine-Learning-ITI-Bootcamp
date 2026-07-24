# NumPy program to compute the weighted of a given array
import numpy as np

arr = np.array([0, 1, 2, 3, 4])

weights = np.array([1, 2, 3, 4, 5]) 

print("Weighted average of the said array:")
print(np.average(arr, weights=weights))