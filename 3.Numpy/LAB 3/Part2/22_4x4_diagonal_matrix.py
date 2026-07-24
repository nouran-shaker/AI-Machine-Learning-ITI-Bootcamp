# NumPy program to create a 2-D array whose diagonal equals [4, 5, 6, 8] and 0's elsewhere
import numpy as np

arr = np.zeros((4, 4), dtype=int)
np.fill_diagonal(arr, [4, 5, 6, 8])

print("Array:")
print(arr)