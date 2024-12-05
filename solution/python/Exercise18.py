import numpy as np

# --- Step 1: Create the adjacency matrix for the directed graph ---
# Adjacency matrix (modify this according to your graph)
# Example: 7 nodes with edges 1->2, 2->3, ..., 6->7
adj_matrix = np.array([
    [0, 1, 0, 0, 0, 0, 0],  # P1 -> P2
    [0, 0, 1, 0, 0, 0, 0],  # P2 -> P3
    [0, 0, 0, 1, 0, 0, 0],  # P3 -> P4
    [0, 0, 0, 0, 1, 0, 0],  # P4 -> P5
    [0, 0, 0, 0, 0, 1, 0],  # P5 -> P6
    [0, 0, 0, 0, 0, 0, 1],  # P6 -> P7
    [0, 0, 0, 0, 0, 0, 0]   # P7 has no outgoing edges
])

# --- Part a: Vertex (Adjacency) Matrix ---
print("Part a: Vertex (Adjacency) Matrix")
print(adj_matrix)
print()

# --- Part b: Number of Paths of Length 3 ---
print("Part b: Number of Paths of Length 3")
# Compute A^3 using numpy.linalg.matrix_power
adj_matrix_cubed = np.linalg.matrix_power(adj_matrix, 3)
# The total number of paths of length 3 is the sum of all entries
num_paths_length_3 = np.sum(adj_matrix_cubed)
print(f"Number of paths of length 3: {num_paths_length_3}")
print()

# --- Part c: Is the Graph Strongly Connected? ---
print("Part c: Is the Graph Connected?")
# Check strong connectivity by verifying if every node is reachable
# from every other node. Use Floyd-Warshall Algorithm for reachability.
n = len(adj_matrix)
reachability = adj_matrix.copy()
for k in range(n):
    for i in range(n):
        for j in range(n):
            reachability[i][j] = reachability[i][j] or (reachability[i][k] and reachability[k][j])
is_connected = np.all(reachability)  # If all entries are 1, the graph is strongly connected
print(f"Is the graph connected? {is_connected}")
print()

# --- Part d: Find All Paths of Length 6 from P7 to P6 ---
print("Part d: Find All Paths of Length 6 from P7 to P6")
# Compute A^6 to find paths of length 6
adj_matrix_sixth = np.linalg.matrix_power(adj_matrix, 6)
# Number of paths from P7 (row 6) to P6 (column 5) (note: 0-based indexing)
num_paths_length_6 = adj_matrix_sixth[6 - 1, 5 - 1]
print(f"Number of paths of length 6 from P7 to P6: {num_paths_length_6}")
print()

# --- Part e: Number of 4-Step Connections from P1 to P3 ---
print("Part e: Number of 4-Step Connections from P1 to P3")
# Compute A^4 to find paths of length 4
adj_matrix_fourth = np.linalg.matrix_power(adj_matrix, 4)
# Number of 4-step connections from P1 to P3 (row 0, column 2)
num_4_step_connections = adj_matrix_fourth[0, 2]
print(f"Number of 4-step connections from P1 to P3: {num_4_step_connections}")
print()

# --- Part f: Find All Cliques of the Graph ---
print("Part f: Find All Cliques of the Graph")
# For a directed graph, "cliques" can be interpreted as nodes that are all
# mutually reachable in some way. A brute-force check can find cliques.
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

# --- Part g: Is the Graph a Tournament? ---
print("Part g: Is the Graph a Tournament Graph?")
# A tournament graph has exactly one directed edge between every pair of nodes
is_tournament = True
for i in range(n):
    for j in range(n):
        if i != j and adj_matrix[i, j] + adj_matrix[j, i] != 1:
            is_tournament = False
            break
print(f"Is the graph a tournament? {is_tournament}")
