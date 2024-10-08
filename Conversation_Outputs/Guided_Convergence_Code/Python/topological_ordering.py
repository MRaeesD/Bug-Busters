def topological_ordering(nodes):
    # Initialize topologically_ordered_nodes with nodes that have no incoming edges
    topologically_ordered_nodes = [node for node in nodes if not node.incoming_nodes]

    for node in topologically_ordered_nodes:
        for outgoing_node in node.outgoing_nodes:
            # Check if all incoming nodes of 'outgoing_node' are already in 'topologically_ordered_nodes'
            # This ensures 'outgoing_node' can be safely added as its dependencies are resolved
            if all(in_node in topologically_ordered_nodes for in_node in outgoing_node.incoming_nodes) and outgoing_node not in topologically_ordered_nodes:
                topologically_ordered_nodes.append(outgoing_node)

    return topologically_ordered_nodes