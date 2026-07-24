# NumPy program to create a 5x5 zero matrix with elements on the main diagonal equal to 1, 2, 3, 4, 5
import numpy as np
zero_matrix = np.zeros((5, 5))
np.fill_diagonal(zero_matrix,[1,2,3,4,5])
print("5x5 zero matrix with diagonal elements 1, 2, 3, 4, 5:")
print(zero_matrix)
