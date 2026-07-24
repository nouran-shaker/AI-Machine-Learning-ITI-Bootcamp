#NumPy program to get the values and indices of the elements that are bigger than 10 in a given array
import numpy as np
given_value=10
arr1=np.array([[0, 10, 20],[20, 30, 40]])
print("Original Array:")
print(arr1)

values_greater_than_10 = arr1[arr1 > given_value]

indices = np.where(arr1 > given_value)

print("Values bigger than ",given_value ," =", values_greater_than_10)

print("Indices of these elements:", indices)