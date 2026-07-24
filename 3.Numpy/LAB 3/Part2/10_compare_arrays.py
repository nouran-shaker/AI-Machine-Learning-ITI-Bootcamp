# NumPy program to test whether each element of a 1-D array is also present in a second array
import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([0, 40])
result = np.isin(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Elements of Array 1 in Array 2:", result)