# NumPy program to test a given array element-wise for finiteness (not infinity or not a number).
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
if np.isfinite(arr1).all():
    print("the array contain only finite elements")
else:
    print("the array contain an infinite or NaN element")
