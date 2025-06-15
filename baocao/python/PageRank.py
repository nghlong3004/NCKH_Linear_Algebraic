import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def pagerank_calc(adj_matrix, d=0.85, max_iter=100, tol=1e-6):
    n = adj_matrix.shape[0]
    adj_matrix = adj_matrix.astype(float)
    out_deg = adj_matrix.sum(axis=0)

    for j in range(n):
        if out_deg[j] == 0:
            adj_matrix[:, j] = 1.0 / n
            out_deg[j] = 1.0

    M = adj_matrix / out_deg
    r = np.full(n, 1.0 / n)
    teleport = np.full(n, 1.0 / n)

    for _ in range(max_iter):
        r_next = (1 - d) * teleport + d * (M @ r)
        if np.linalg.norm(r_next - r, 1) < tol:
            break
        r = r_next
    return r

# --- Step 1: Input from user ---
n = int(input("Enter number of nodes: "))
nodes = []
print("Enter node names:")
for i in range(n):
    nodes.append(input(f"  Node {i+1}: "))

adj_matrix = np.zeros((n, n), dtype=int)

print("\nEnter directed links (e.g., An -> Binh). Type 'done' to finish.")
while True:
    line = input("Link: ")
    if line.strip().lower() == 'done':
        break
    try:
        src, dst = map(str.strip, line.split("->"))
        i, j = nodes.index(src), nodes.index(dst)
        adj_matrix[j][i] = 1  # Column = source, Row = target
    except:
        print("Invalid input. Please use format 'Source -> Target'.")

# --- Step 2: Calculate PageRank ---
pagerank_vector = pagerank_calc(adj_matrix)

# --- Step 3: Output results ---
print("\n--- Final PageRank ---")
for name, score in zip(nodes, pagerank_vector):
    print(f"{name:8s}: {score:.4f}")
print("Total:", np.sum(pagerank_vector))

# --- Step 4: Draw graph ---
G = nx.DiGraph()
for i, src in enumerate(nodes):
    for j, dst in enumerate(nodes):
        if adj_matrix[j][i] == 1:
            G.add_edge(src, dst)

pos = nx.spring_layout(G, seed=42, k=1.0)
plt.figure(figsize=(8, 6))

nx.draw_networkx_nodes(G, pos, node_size=2800, node_color='lightblue', edgecolors='black')
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True, arrowsize=20, width=2, connectionstyle="arc3,rad=0.08")
nx.draw_networkx_labels(G, pos, font_size=11, font_weight='bold')

pr_labels = {node: f'PR={pagerank_vector[nodes.index(node)]:.3f}' for node in nodes}
offset_pos = {node: (x, y - 0.10) for node, (x, y) in pos.items()}
nx.draw_networkx_labels(G, offset_pos, labels=pr_labels, font_size=10, font_color='darkgreen')

plt.title("Custom Network and PageRank", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
