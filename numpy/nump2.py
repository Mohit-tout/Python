import numpy as np
from numpy.linalg import eig

A = np.array([[2, 0],
              [0, 3]])

eigenvalues, eigenvectors = eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)