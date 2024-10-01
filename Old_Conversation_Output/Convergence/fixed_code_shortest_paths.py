def shortest_paths(source, weight_by_edge):
    # Gather all unique nodes from the edges for initialization
    nodes = set([node for edge in weight_by_edge for node in edge])
    weight_by_node = {
        node: float('inf') for node in nodes
    }
    weight_by_node[source] = 0

    # Relaxation step of the Bellman-Ford algorithm
    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            # Correctly update weight_by_node instead of weight_by_edge
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    # Check for negative-weight cycles for robustness
    for (u, v), weight in weight_by_edge.items():
        if weight_by_node[u] + weight < weight_by_node[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return weight_by_node