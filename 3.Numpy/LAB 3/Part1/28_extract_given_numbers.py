# NumPy program to extract all numbers from a given array less and greater than a specified number
import numpy as np
specified = 5
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
less_than_specified = arr[arr < specified]
greater_than_specified = arr[arr > specified]
print("Numbers less than", specified, ":", less_than_specified)
print("Numbers greater than", specified, ":", greater_than_specified)
