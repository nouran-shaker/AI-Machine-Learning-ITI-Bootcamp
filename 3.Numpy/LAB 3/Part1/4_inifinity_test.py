# NumPy program to test elements-wise for positive or negative infinity
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5, np.inf, -np.inf])
if np.isinf(arr1).any():
    print("the array contain an infinite element")
else:
    print("the array contain only finite elements")
    
