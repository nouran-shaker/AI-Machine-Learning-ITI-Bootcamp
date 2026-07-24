# NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last
import numpy as np
arr1 = np.arange(15, 56)
print("Vector with values ranging from 15 to 55:")
print(arr1[1:-1])