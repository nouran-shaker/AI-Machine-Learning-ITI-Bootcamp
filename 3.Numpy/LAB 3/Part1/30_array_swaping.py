# NumPy program to create a 4x4 array. Create an array from said array by swapping first and last, second and third columns
import numpy as np
arr=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print("Original array:")
print(arr)
# Swap first and last columns
arr[:, [0, 3]] = arr[:, [3, 0]]
# Swap second and third columns
arr[:, [1, 2]] = arr[:, [2, 1]]
print("Array after swapping columns:")
print(arr)