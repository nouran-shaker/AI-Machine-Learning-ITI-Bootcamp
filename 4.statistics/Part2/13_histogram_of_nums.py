# NumPy program to compute the histogram of nums against the bins
import numpy as np

nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])

print("Result:")
print(np.histogram(nums, bins))