#Program to find the value of x for: AX=B ,given A and B matrices
import numpy as np

A = np.array([[3, 1], 
              [1, 2]])
b = np.array([9, 8])

# Solve the linear system using np.linalg.solve()
x = np.linalg.solve(A, b)

print("Solution for x:", x)