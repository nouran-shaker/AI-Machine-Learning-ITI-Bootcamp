#NumPy program to find the set difference between two arrays. The set difference will return sorted, distinct values in array1 that are not in array2
import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
array2 = np.array([10, 30, 40 , 50, 70,90])
set_difference = np.setdiff1d(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Set difference between Array 1 and Array 2:", set_difference)