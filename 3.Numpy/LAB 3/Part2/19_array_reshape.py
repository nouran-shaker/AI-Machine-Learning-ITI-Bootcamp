# NumPy program to create another shape from an array without changing its data
import numpy as np
arr1=np.arange(1,7)
reshaped_3x2=np.reshape(arr1,(3,2))
reshaped_2x3=np.reshape(arr1,(2,3))

print("Original array:",arr1)
print("Reshape 3x2:",reshaped_3x2)
print("Reshape 2x3:",reshaped_2x3)
