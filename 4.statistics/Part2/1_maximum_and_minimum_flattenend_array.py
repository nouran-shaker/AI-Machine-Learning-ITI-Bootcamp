#Python program to find the maximum and minimum value of a given flattened array
import numpy as np

arr = np.array([[0, 1], [2, 3]])

print("Maximum value of the above flattened array:")
print(np.max(arr))

print("Minimum value of the above flattened array:")
print(np.min(arr))