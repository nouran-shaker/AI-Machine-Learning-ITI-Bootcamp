# A NumPy program to create a 2-dimensional array of size 2 x 3
# composed of 4-byte integer elements, and print its shape, type, and data type.
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

print("Array:", arr)
print("Shape:", arr.shape)
print("Type:", type(arr))
print("Data type:", arr.dtype)
