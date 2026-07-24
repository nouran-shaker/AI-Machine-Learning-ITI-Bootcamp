#NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array
import numpy as np
centigrade = np.array([-17.78, -11.11, 7.34, 1.11, 37.73,0])
fahrenheit = (centigrade * 9/5) + 32
print("Centigrade values:", centigrade)
print("Fahrenheit values:", np.round(fahrenheit, 2))