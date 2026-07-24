#NumPy program to compute the 80th percentile for all elements in a given array along the second axis
import numpy as np

arr = np.array([1.0, 2.0, 3.0, 4.0])

print("80th percentile for all elements in the given array:")
print(np.percentile(arr, 80))