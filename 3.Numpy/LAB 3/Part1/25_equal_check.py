# NumPy program to check whether two arrays are equal (element wise) or not
import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 2, 3, 4, 5])
are_equal = np.array_equal(array1, array2)
if are_equal:
    print("The two arrays are equal (element wise).")
else:
    print("The two arrays are not equal (element wise).")