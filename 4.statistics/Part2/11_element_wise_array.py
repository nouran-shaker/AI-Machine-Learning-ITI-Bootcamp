# NumPy program to test element-wise of a given array for finiteness (not infinity or not Not a Number), positive or negative infinity, for NaN, for NaT (not a time), for negative infinity, for positive infinity
import numpy as np

print("Test element-wise for finiteness:")
print(np.isfinite(np.array([1, 0, np.nan])))

print("Test element-wise for positive or negative infinity:")
print(np.isinf(np.array([np.inf, 0, -np.inf])))

print("Test element-wise for NaN:")
print(np.isnan(np.array([np.nan, 1, 0])))

print("Test element-wise for NaT (not a time):")
print(np.isnat(np.array(['NaT', '2023-01-01'], dtype='datetime64[ns]')))

print("Test element-wise for negative infinity:")
print(np.isneginf(np.array([-np.inf, 0, 1])))

print("Test element-wise for positive infinity:")
print(np.isposinf(np.array([1, 0, np.inf])))