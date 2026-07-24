# NumPy program to get the unique elements of an array
import numpy as np
array = np.array([10, 10, 20, 20, 30, 30])
unique_elements = np.unique(array)
array2=np.array([[1, 1], [2, 3]])
unique_elements2 = np.unique(array2)

print("Array:", array)
print("Unique elements:", unique_elements)
print("Array2:", array2)
print("Unique elements in Array2:", unique_elements2)