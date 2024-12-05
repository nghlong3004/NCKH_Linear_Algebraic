import numpy as np

# Define the adjacency matrix A
A = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
])

# Compute A^2 and A^3
A2 = np.linalg.matrix_power(A, 2)
A3 = np.linalg.matrix_power(A, 3)

# Extract the required values
first_row_A2 = A2[0]  # First row of A^2 (walks of length 2 starting at V1)
walks_length_3_V2_to_V4 = A3[1, 3]  # Walks of length 3 from V2 to V4
walks_upto_3_V2_to_V4 = A[1, 3] + A2[1, 3] + A3[1, 3]  # Sum of walks of length 1, 2, and 3

# Print results
print("Adjacency Matrix A^2:")
print(A2)

print("\nFirst row of A^2 (walks of length 2 starting from V1):")
print(first_row_A2)

print(f"\nNumber of walks of length 3 from V2 to V4: {walks_length_3_V2_to_V4}")
print(f"Number of walks of length less than or equal to 3 from V2 to V4: {walks_upto_3_V2_to_V4}")
