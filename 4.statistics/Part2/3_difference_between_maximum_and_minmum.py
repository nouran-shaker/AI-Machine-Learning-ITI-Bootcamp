#NumPy program to calculate the difference between the maximum and the minimum values of a given array along the second axis
import numpy as np

arr = np.array([[0, 1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10, 11]])

print("Difference between the maximum and the minimum values of the said array:")

print(np.ptp(arr, axis=1))