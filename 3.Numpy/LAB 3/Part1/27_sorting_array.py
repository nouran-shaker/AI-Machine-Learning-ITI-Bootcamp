#NumPy program to sort a given array by row and column in ascending order
import numpy as np
arr = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
# Sort by row
sorted_by_row=np.sort(arr,axis=1)
#sort by column
sorted_by_column=np.sort(arr,axis=0)
print("Original array:")
print(arr)
print("Array sorted by row:")
print(sorted_by_row)
print("Array sorted by column:")
print(sorted_by_column)

