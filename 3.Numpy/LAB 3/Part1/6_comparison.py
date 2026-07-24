#NumPy program to create an element-wise comparison
import numpy as np
arr1 = np.array([1,7, 3, 4, 5])
arr2 = np.array([1, 2, 0, 4, 5])
result1 = np.less(arr1, arr2)
result2 = np.greater(arr1, arr2)
print("Element-wise comparison of two arrays:")
print(result1)
print("Element-wise comparison of two arrays:")
print(result2)