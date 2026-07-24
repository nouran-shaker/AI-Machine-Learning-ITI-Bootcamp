#NumPy program to sort along the first and last axes of an array
import numpy as np
array = np.array([[2 ,1], [4,6]])
sorted_first_axis = np.sort(array, axis=0)
sorted_last_axis = np.sort(array, axis=1)
print("original array:",array)
print("Sort along the first axis:",sorted_first_axis)
print("Sort along the last axis:",sorted_last_axis)