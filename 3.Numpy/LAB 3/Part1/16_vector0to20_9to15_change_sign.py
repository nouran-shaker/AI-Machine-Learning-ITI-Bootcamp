# NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15
import numpy as np 
arr1=np.arange(0,21)
arr1[9:16]=-arr1[9:16]
print("Vector with values from 0 to 20 and changed sign of numbers in the range from 9 to 15:")
print(arr1)
