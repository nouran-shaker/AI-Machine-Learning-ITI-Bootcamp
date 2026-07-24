# NumPy program to replace all numbers in a given array equal, less and greater than a given number
import numpy as np

given_number = 3
arr = np.array([1, 2, 3, 4, 5])

arr[arr < given_number] = -1
arr[arr > given_number] = 1
arr[arr == given_number] = 0

print("Array after replacing numbers equal, less and greater than", given_number, ":", arr)
