import numpy as np

# Vector
v = np.array([2, 3])
w = np.array([1, 0, 5])

# Matrix
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

# Addition
C = A + B

# Matrix Multiplication (Dot Product)
D = np.dot(A, B)

# Transpose
A_T = A.T

# Inverse
A_inv = np.linalg.inv(A)

# Determinant
det_A = np.linalg.det(A)

print("Addition:\n", C)
print("Multiplication:\n", D)