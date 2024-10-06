def shortest_paths(source, weight_by_edge):
    # Get all unique nodes from the edge list
    unique_nodes = set()
    for u, v in weight_by_edge.keys():
        unique_nodes.update((u, v))
        
    # Initialize weight_by_node with infinity for each node
    weight_by_node = {v: float('inf') for v in unique_nodes}
    weight_by_node[source] = 0

    for _ in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight

    return weight_by_node