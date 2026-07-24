# NumPy program to compare two arrays using NumPy
import numpy as np
array_a=np.array([1,2])
array_b=np.array([4,5])
print("Array A:", array_a)
print("Array B:", array_b)
greater_than = np.greater(array_a, array_b)
print("Array A > Array B:", greater_than)
greater_equal = np.greater_equal(array_a, array_b)
print("Array A >= Array B:", greater_equal)
less_than = np.less(array_a, array_b)
print("Array A < Array B:", less_than)
less_equal = np.less_equal(array_a, array_b)
print("Array A <= Array B:", less_equal)
