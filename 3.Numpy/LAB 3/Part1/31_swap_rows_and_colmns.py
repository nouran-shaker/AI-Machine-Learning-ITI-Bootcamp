#NumPy program to swap rows and columns of a given array in reverse order
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array:")
print(arr)
# Swap rows and columns in reverse order
swapped_arr = arr[::-1, ::-1]
print("Array after swapping rows and columns in reverse order:")
print(swapped_arr)
