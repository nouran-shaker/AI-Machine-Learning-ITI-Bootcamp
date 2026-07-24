#Program to Compute element-wise addition, subtraction, and dot product.
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vector a:", a)
print("Vector b:", b)

# Element-wise addition
addition = a + b
print("\nElement-wise Addition:", addition)

# Element-wise subtraction
subtraction = a - b
print("Element-wise Subtraction:", subtraction)

# Dot product
dot_prod = np.dot(a, b)
print("Dot Product:", dot_prod)