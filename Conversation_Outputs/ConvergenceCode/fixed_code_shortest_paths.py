def shortest_paths(source, weight_by_edge):
    # Initialize weight_by_node for all nodes, not just target nodes
    weight_by_node = {u: float('inf') for u, _ in weight_by_edge}
    weight_by_node.update({v: float('inf') for _, v in weight_by_edge})
    weight_by_node[source] = 0

    # Perform relaxation for |V| - 1 iterations
    for i in range(len(weight_by_node) - 1):
        updated = False
        for (u, v), weight in weight_by_edge.items():
            # Update weight_by_node[v] instead of weight_by_edge[u, v]
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight
                updated = True
        # Early termination if no updates were made
        if not updated:
            break

    # Negative cycle detection
    for (u, v), weight in weight_by_edge.items():
        if weight_by_node[u] + weight < weight_by_node[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    return weight_by_node