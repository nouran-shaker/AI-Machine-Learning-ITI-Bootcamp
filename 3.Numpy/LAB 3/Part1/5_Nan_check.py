# NumPy program to test elements-wise for NaN of a given array
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5, np.nan])
if np.isnan(arr1).any():
    print("the array contain a NaN element")
else:
    print("the array contain only non-NaN elements")
    