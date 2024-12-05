import numpy as np

# Define the consumption matrix A
A = np.array([
    [0.2, 0.1, 0.3],
    [0.2, 0.7, 0.1],
    [0.3, 0.2, 0.5]
])

# Total consumption vector c (the sum of each column in the matrix A)
# In this case, the total consumption should be 1 for each commodity as described in the problem.
c = np.array([1, 1, 1])  # Each commodity is consumed in total by all individuals

# Solve the system A * x = c for the production vector x
# We will use np.linalg.solve to solve this system
production_vector = np.linalg.solve(A, c)

# Output the results
print("Production Vector (x1, x2, x3):")
print(production_vector)
