import numpy as np

# Coefficient matrix
A = np.array([
    [1, 0, 0, -1],  # Equation 1
    [0, 0, -1, 1],  # Equation 2
    [0, -1, 1, 0],  # Equation 3
    [-1, 1, 0, 0]   # Equation 4
])

# Constant terms
B = np.array([-130, -60, 240, -50])

# Check dimensions
print(f"A shape: {A.shape}")
print(f"B shape: {B.shape}")

# Check if the matrix is singular (determinant = 0)
det = np.linalg.det(A)
print(f"Determinant of A: {det}")

# Solve using least squares if matrix is singular
if det == 0:
    print("Matrix is singular, using least squares solution instead.")
    X, _, _, _ = np.linalg.lstsq(A, B, rcond=None)
else:
    # Solve the system of linear equations
    X = np.linalg.solve(A, B)

# Output the results
x1, x2, x3, x4 = X
print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")
print(f"x3 = {x3:.2f}")
print(f"x4 = {x4:.2f}")
