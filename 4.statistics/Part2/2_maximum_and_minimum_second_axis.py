#NumPy program to get the minimum and maximum value of a given array along the second axis
import numpy as np

arr = np.array([[0, 1], [2, 3]])

print("Maximum value along the second axis:")
print(np.max(arr, axis=1))

print("Minimum value along the second axis:")
print(np.min(arr, axis=1))