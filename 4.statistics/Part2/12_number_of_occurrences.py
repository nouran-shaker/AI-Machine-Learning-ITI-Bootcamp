# Python program to count number of occurrences of each value in a given array of non-negative integers
import numpy as np

arr = np.array([0, 1, 6, 1, 4, 1, 2, 2, 7])

print("Number of occurrences of each value in array:")
print(np.bincount(arr))