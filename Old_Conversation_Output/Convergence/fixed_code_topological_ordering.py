def topological_ordering(nodes):
    # Initialize the in-degree count for each node
    in_degree = {node: 0 for node in nodes}
    for node in nodes:
        for nextnode in node.outgoing_nodes:
            in_degree[nextnode] += 1

    # Initialize the queue with nodes having no incoming edges
    queue = [node for node in nodes if in_degree[node] == 0]
    ordered_nodes = []

    while queue:
        node = queue.pop(0)
        ordered_nodes.append(node)
        for nextnode in node.outgoing_nodes:
            in_degree[nextnode] -= 1
            if in_degree[nextnode] == 0:
                queue.append(nextnode)

    # Check if the graph has a cycle
    if len(ordered_nodes) != len(nodes):
        raise ValueError("The graph has at least one cycle")

    return ordered_nodes