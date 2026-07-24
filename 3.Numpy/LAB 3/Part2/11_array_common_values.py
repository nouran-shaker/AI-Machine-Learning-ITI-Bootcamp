# NumPy program to find common values between two arrays
import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([10, 30, 40])
common_values = np.intersect1d(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Common values between Array 1 and Array 2:", common_values)
