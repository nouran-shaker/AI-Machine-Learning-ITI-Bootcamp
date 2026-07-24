#NumPy program to find the number of rows and columns in a given matrix
import numpy as np
matrix=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Number of rows:", matrix.shape[0])
print("Number of columns:", matrix.shape[1])