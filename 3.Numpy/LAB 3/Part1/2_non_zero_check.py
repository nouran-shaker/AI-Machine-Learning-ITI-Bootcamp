#NumPy program to test if any of the elements of a given array are non-zero
import numpy as np
arr1=np.array([0,0,0,0,0])
if np.any(arr1)==True :
    print ("the array contain a non-zero element")
else :
    print ("All elements of array are zero")