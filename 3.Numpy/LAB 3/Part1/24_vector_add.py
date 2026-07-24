#NumPy program to add a vector to each row of a given matrix
import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 0, 1])
result = matrix + vector
print("Resultant matrix after adding the vector to each row:")
print(result)