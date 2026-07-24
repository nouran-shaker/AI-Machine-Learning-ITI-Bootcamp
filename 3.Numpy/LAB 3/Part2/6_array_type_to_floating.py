#NumPy program to convert an array to a floating type
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr_float = arr.astype(float)
print("Original array:", arr)
print("Array converted to floating type:", arr_float)
