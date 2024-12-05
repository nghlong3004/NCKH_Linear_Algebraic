import numpy as np

# Step 1: Define the adjacency matrix A for the graph
A = np.array([
    [0, 1, 0, 1, 0, 0, 0, 0],  # V1
    [1, 0, 1, 0, 0, 0, 0, 0],  # V2
    [0, 1, 0, 1, 0, 1, 0, 0],  # V3
    [1, 0, 1, 0, 1, 0, 0, 0],  # V4
    [0, 0, 0, 1, 0, 0, 1, 1],  # V5
    [0, 0, 1, 0, 0, 0, 0, 1],  # V6
    [0, 0, 0, 0, 1, 0, 0, 1],  # V7
    [0, 0, 0, 0, 1, 1, 1, 0]   # V8
])

# Step 2: Compute A^2
A2 = np.matmul(A, A)  # A^2 = A * A

# Step 3: Functions to calculate walks for any A^n
def print_walks(A_matrix, walk_length):
    print(f"\nWalks of length {walk_length}:")
    for i in range(len(A_matrix)):
        for j in range(len(A_matrix)):
            print(f"Walks from V{i+1} to V{j+1}: {A_matrix[i, j]}")

# Check for walks of length 2, 4, 6, and 8 from the adjacency matrix
print_walks(A2, 2)

# Step 4: Compute A^4, A^6, A^8 and analyze walks
A4 = np.matmul(A2, A2)  # A^4 = A^2 * A^2
A6 = np.matmul(A2, A4)  # A^6 = A^2 * A^4
A8 = np.matmul(A2, A6)  # A^8 = A^2 * A^6

# Print results for walks of length 4, 6, and 8
print_walks(A4, 4)
print_walks(A6, 6)
print_walks(A8, 8)

# Step 5: Compute walks for odd lengths (3, 5, 7)
def print_odd_walks(A_matrix, walk_length):
    print(f"\nWalks of odd length {walk_length}:")
    for i in range(len(A_matrix)):
        for j in range(len(A_matrix)):
            print(f"Walks from V{i+1} to V{j+1}: {A_matrix[i, j]}")

# A^3, A^5, A^7
A3 = np.matmul(A2, A)  # A^3 = A^2 * A
A5 = np.matmul(A2, A3)  # A^5 = A^2 * A^3
A7 = np.matmul(A2, A5)  # A^7 = A^2 * A^5

print_odd_walks(A3, 3)
print_odd_walks(A5, 5)
print_odd_walks(A7, 7)

# Step 6: Conjectures
# A simple check for walks based on even and odd combinations of i, j, k
countEven = 0
countOdd = 0
def conjecture_walks(A_matrix, k):
    print(f"\nChecking walks for length {k} based on i + j + k even or odd:")
    for i in range(len(A_matrix)):
        for j in range(len(A_matrix)):
            total = (i + 1) + (j + 1) + k
            if total % 2 == 0:
                print(f"Walk from V{i+1} to V{j+1} with length {k} (even): {A_matrix[i, j]}")
            else:
                print(f"Walk from V{i+1} to V{j+1} with length {k} (odd): {A_matrix[i, j]}")

conjecture_walks(A2, 2)
conjecture_walks(A3, 3)

# Step 7: Modify the graph (add edges {V3, V6}, {V5, V8})
# Add edges to the graph
A[2, 5] = A[5, 2] = 1  # Add edge {V3, V6}
A[4, 7] = A[7, 4] = 1  # Add edge {V5, V8}

print("\nNew adjacency matrix B after adding edges {V3, V6} and {V5, V8}:")
print(A)

# Recompute powers of the new adjacency matrix
A2_new = np.matmul(A, A)  # New A^2
A4_new = np.matmul(A2_new, A2_new)  # New A^4
A6_new = np.matmul(A2_new, A4_new)  # New A^6
A8_new = np.matmul(A2_new, A6_new)  # New A^8

# Print results for the new graph
print_walks(A2_new, 2)
print_walks(A4_new, 4)
print_walks(A6_new, 6)
print_walks(A8_new, 8)
