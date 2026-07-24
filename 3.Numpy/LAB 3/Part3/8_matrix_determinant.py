#  Program to calculate the determinant of the matrix
import numpy as np

matrix = np.array([[1, 2], 
                   [3, 4]])

determinant = np.linalg.det(matrix)

print("Determinant:%.2f" % determinant)