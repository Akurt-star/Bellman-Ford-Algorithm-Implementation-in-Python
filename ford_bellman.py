import networkx as nx
import matplotlib.pyplot as plt

# -------------------------------
# Define two directed graphs (G and A) for testing
# G has no negative weight cycles
# A contains a negative weight cycle (B → C → D → B)
# -------------------------------

# Graph G (no negative cycle)
G = nx.DiGraph()
edges = [
    ("A", "B", 2),    # positive edge
    ("B", "C", -5),   # negative edge
    ("C", "D", 2),    # positive edge
    ("D", "B", 4),    # cycle B→C→D→B has weight -5 + 2 + 4 = +1 (not negative)
    ("A", "E", 3),    # positive edge
    ("E", "D", 1),    # positive edge
    ("D", "F", 2),    # positive edge
]
G.add_weighted_edges_from(edges, weight="weight")

# Graph A (contains a negative cycle)
A = nx.DiGraph()
edges = [
    ("A", "B", 2),    # positive edge
    ("B", "C", -5),   # negative edge
    ("C", "D", 2),    # positive edge
    ("D", "B", 2),    # cycle B→C→D→B has weight -5 + 2 + 2 = -1 (negative cycle)
    ("A", "E", 3),    # positive edge
    ("E", "D", 1),    # positive edge
    ("D", "F", 2),    # positive edge
]
A.add_weighted_edges_from(edges, weight="weight")

# -------------------------------
# Bellman-Ford Algorithm Implementation
# -------------------------------
def ford_bellman(graph, source, show_relax=False):
    """
    Bellman-Ford algorithm implementation.

    Parameters
    ----------
    graph : networkx.DiGraph
        Input directed graph with weighted edges.
    source : node
        Starting node for shortest paths.
    show_relax : bool, optional (default=False)
        If True, prints details when a relaxation step updates a distance.

    Returns
    -------
    dict or None
        Dictionary of shortest distances and paths from source to every node.
        Returns None if a negative weight cycle is detected.
    """

    # Initialize distances and paths
    shortest_paths_dict = {
        node: {"distance": float('inf'), "path": []} for node in graph.nodes()
    }
    shortest_paths_dict[source]["distance"] = 0
    shortest_paths_dict[source]["path"] = [source]

    # Relax all edges |V|-1 times
    for _ in range(len(graph.nodes) - 1):
        updated = False  # flag to check if any edge was relaxed
        for u, v, edge in graph.edges(data=True):
            # Relaxation step
            if shortest_paths_dict[u]["distance"] + edge["weight"] < shortest_paths_dict[v]["distance"]:
                shortest_paths_dict[v]["distance"] = shortest_paths_dict[u]["distance"] + edge["weight"]
                shortest_paths_dict[v]["path"] = shortest_paths_dict[u]["path"] + [v]
                updated = True
                if show_relax:
                    print(f"Relaxed edge {u}->{v}, new distance for {v}: {shortest_paths_dict[v]['distance']}")
        if not updated:
            break  # no update in this pass → stop early

    # Check for negative weight cycles
    for u, v, edge in graph.edges(data=True):
        if shortest_paths_dict[u]["distance"] + edge["weight"] < shortest_paths_dict[v]["distance"]:
            print("There is a negative edge cycle in the graph.")
            return None

    return shortest_paths_dict


# -------------------------------
# Run Bellman-Ford on both graphs
# -------------------------------
print("Graph G (no negative cycle):")
print(ford_bellman(G, "A"))

print("\nGraph A (with negative cycle):")
print(ford_bellman(A, "A"))

# -------------------------------
# Visualization of graph G
# -------------------------------
pos = nx.spring_layout(G)  # compute layout for visualization
nx.draw(G, pos, with_labels=True, node_color="lightblue")

# Draw edge weights as labels
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
