#NumPy program to reverse an array (the first element becomes the last)
import numpy as np
arr=np.arange(12,38)
reversed_arr=arr[::-1]
print("Original array:", arr)
print("Reversed array:", reversed_arr)
