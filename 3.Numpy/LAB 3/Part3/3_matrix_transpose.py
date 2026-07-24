#Program to calculate the transpose of a matrix
import numpy as np

matrix = np.array([[1, 2], 
                   [3, 4], 
                   [5, 6]])

# Transpose the matrix using the .T attribute
transposed_matrix = matrix.T

print("Original Matrix: ", matrix)
print("Transposed Matrix: ", transposed_matrix)