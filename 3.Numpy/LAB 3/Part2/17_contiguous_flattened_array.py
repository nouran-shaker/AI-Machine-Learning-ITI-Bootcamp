# NumPy program to create a contiguous flattened array
import numpy as np 
arr=np.array([[10, 20, 30],
             [20, 40, 50]])
flattened_array=np.reshape(arr,-1)
print("Original array:",arr)
print("New flattened array:",flattened_array)
