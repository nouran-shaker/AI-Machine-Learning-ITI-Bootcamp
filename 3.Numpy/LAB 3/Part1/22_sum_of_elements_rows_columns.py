# NumPy program to compute the sum of all elements, the sum of each column and the sum of each row in a given array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Sum of all elements
total_sum=np.sum(arr)
# Sum of each column
column_sum=np.sum(arr,axis=0)
# Sum of each row
rows_sum=np.sum(arr,axis=1)
print("Sum of all elements:", total_sum)
print("Sum of each column:", column_sum)
print("Sum of each row:", rows_sum)
