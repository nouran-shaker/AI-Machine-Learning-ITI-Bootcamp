#NumPy program to find the 4th element of a specified array
import numpy as np 

required_element=4

arr=np.array([2, 4, 6 ,6, 8, 10])
element=arr[required_element-1]

print(required_element,"th element of the array",element)
