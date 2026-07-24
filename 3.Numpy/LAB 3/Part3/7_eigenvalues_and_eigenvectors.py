#Program to find eigenvalues and eigenvectors of the matrix
import numpy as np

matrix = np.array([[2, -1], 
                   [-1, 2]])

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)