#Program to calculate the inverse of a matrix
import numpy as np

matrix = np.array([[4, 7], 
                   [2, 6]])

inverse_matrix = np.linalg.inv(matrix)

print("Inverse Matrix:", inverse_matrix)