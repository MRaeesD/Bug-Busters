def topological_ordering(nodes):
    ordered_nodes = [node for node in nodes if not node.incoming_nodes]

    for node in ordered_nodes:
        for nextnode in node.outgoing_nodes:
            if set(nextnode.incoming_nodes).issubset(ordered_nodes) and nextnode not in ordered_nodes:  # Change made here
                ordered_nodes.append(nextnode)

    return ordered_nodes
