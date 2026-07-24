# NumPy program to append values to the end of an array
import numpy as np
arr = np.array([10 , 20, 30])
values_to_append = np.arange(40, 100, 10)
arr = np.append(arr, values_to_append)
print("Original array:", np.array([10 , 20, 30]))
print("Array after appending values:", arr)