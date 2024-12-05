import numpy as np

# Coefficients matrix (3x4, fewer equations than variables)
coefficients = np.array([
    [2000, 1000, 1000, 500],
    [5000, 2500, 2000, 1000],
    [1000, 400, 400, 200]
])

# Total cost vector
totals = np.array([29000, 70500, 13600])

# Use np.linalg.lstsq to find the least-squares solution to the underdetermined system
unit_costs, residuals, rank, s = np.linalg.lstsq(coefficients, totals, rcond=None)

# Print the solution
print("Unit costs of products A, B, C, D:", np.round(unit_costs))
