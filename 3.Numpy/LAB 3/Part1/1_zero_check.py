#NumPy program to test whether none of the elements of a given array are zero
import numpy as np 
arr1=np.array([1,2,3,4,5])
if np.all(arr1)==False :
 print ("the array contain a zero")
else :
 print ("None of the elements of array are zero")