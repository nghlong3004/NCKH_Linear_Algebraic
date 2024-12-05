import numpy as np

# --- Step 1: Define the adjacency matrix ---
adj_matrix = np.array([
    [0, 0, 1, 1, 1],  # P1
    [0, 0, 1, 0, 1],  # P2
    [1, 0, 0, 0, 1],  # P3
    [0, 0, 1, 0, 1],  # P4
    [1, 1, 1, 0, 0],  # P5
])

# --- Part a: Draw the Graph (Representation as Adjacency Matrix) ---
print("Part a: Adjacency Matrix Representation")
print(adj_matrix)
print()

# --- Part b: Find All Paths of Length 3 from P1 to P2 ---
print("Part b: Paths of Length 3 from P1 to P2")

# Compute A^3 using numpy.linalg.matrix_power
adj_matrix_cubed = np.linalg.matrix_power(adj_matrix, 3)

# The number of paths of length 3 from P1 to P2 is in adj_matrix_cubed[0, 1] (0-based indexing)
num_paths_3_steps = adj_matrix_cubed[0, 1]
print(f"Number of paths of length 3 from P1 to P2: {num_paths_3_steps}")
print()

# --- Part c: Check if the Graph is Connected ---
print("Part c: Is the Graph Connected?")

# Use Floyd-Warshall algorithm to compute reachability between all nodes
n = adj_matrix.shape[0]
reachability = adj_matrix.copy()

# Floyd-Warshall algorithm to compute transitive closure (reachability)
for k in range(n):
    for i in range(n):
        for j in range(n):
            reachability[i, j] = reachability[i, j] or (reachability[i, k] and reachability[k, j])

# Check if the graph is connected (strongly connected)
is_connected = np.all(reachability)  # If all values are 1, it's connected
print(f"Is the graph connected? {is_connected}")
print()

# --- Part d: Find All Loops of Length 4 from P1 to P1 ---
print("Part d: Find All Loops of Length 4 from P1 to P1")

# Compute A^4 to find paths of length 4
adj_matrix_fourth = np.linalg.matrix_power(adj_matrix, 4)

# The number of loops of length 4 from P1 to P1 is in adj_matrix_fourth[0, 0]
num_loops_4_steps = adj_matrix_fourth[0, 0]
print(f"Number of loops of length 4 from P1 to P1: {num_loops_4_steps}")
print()

# --- Part e: Find the Number of All 4-Step Connections from P1 to P2 ---
print("Part e: Number of 4-Step Connections from P1 to P2")

# The number of 4-step connections from P1 to P2 is in adj_matrix_fourth[0, 1]
num_4_step_connections = adj_matrix_fourth[0, 1]
print(f"Number of 4-step connections from P1 to P2: {num_4_step_connections}")
print()

# --- Part f: Find All Cliques of the Graph ---
print("Part f: Finding All Cliques")

def find_cliques(matrix):
    n = len(matrix)
    cliques = []
    # Brute-force all subsets of nodes
    for subset in range(1, 1 << n):  # All subsets of nodes
        nodes = [i for i in range(n) if (subset & (1 << i))]
        # Check if the subset forms a clique
        if all(matrix[i, j] for i in nodes for j in nodes if i != j):
            cliques.append(nodes)
    return cliques

cliques = find_cliques(adj_matrix)
print(f"All cliques in the graph (node indices): {cliques}")
print()

# --- Part g: Is the Graph a Tournament Graph? ---
print("Part g: Is the Graph a Tournament Graph?")

# A tournament graph has exactly one directed edge between every pair of nodes.
is_tournament = True
for i in range(n):
    for j in range(n):
        if i != j and adj_matrix[i, j] + adj_matrix[j, i] != 1:
            is_tournament = False
            break

print(f"Is the graph a tournament? {is_tournament}")
