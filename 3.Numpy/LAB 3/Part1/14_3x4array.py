# NumPy program to create a 3x4 array and iterate over it
import numpy as np

arr1 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]])

print("3x4 Array:")
print(arr1)

print("\nIterating over the array:")
for i in range(arr1.shape[0]):
    for j in range(arr1.shape[1]):
        print(f"Element at ({i}, {j}): {arr1[i, j]}")
