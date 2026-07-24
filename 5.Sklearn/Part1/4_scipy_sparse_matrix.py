import numpy as np
from scipy import sparse


eye_matrix = np.eye(4)
print("NumPy Array:", eye_matrix)


sparse_matrix = sparse.csr_matrix(eye_matrix)
print("SciPy Sparse Matrix in CSR format:", sparse_matrix)