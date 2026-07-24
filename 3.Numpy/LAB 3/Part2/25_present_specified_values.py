#NumPy program to test whether specified values are present in an array
import numpy as np

original_array = np.array([[1.12, 2.0, 3.45], 
                           [2.33, 5.12, 6.0]])


values_to_test = [2.0, 10.0, 6.0, 4.5, 3.45]

results = np.isin(values_to_test, original_array)


for result in results:
    print(result)