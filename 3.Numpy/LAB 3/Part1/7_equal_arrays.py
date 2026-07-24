#Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
import numpy as np

array1 = np.array([10.0, 20.0, 30.000001, 40.0])
array2 = np.array([10.0, 20.0, 30.000000, 41.0])

print("Array 1:", array1)
print("Array 2:", array2)

exact_equal = np.equal(array1, array2)
print("\nExact element-wise equality:")
print(exact_equal)

equal_with_tolerance = np.isclose(array1, array2)
print("\nElement-wise equality within tolerance:")
print(equal_with_tolerance)
