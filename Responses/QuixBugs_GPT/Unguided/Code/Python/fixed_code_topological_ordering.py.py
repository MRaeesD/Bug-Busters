def topological_ordering(nodes):
    from collections import deque

    ordered_nodes = []
    zero_incoming = deque(node for node in nodes if not node.incoming_nodes)

    while zero_incoming:
        node = zero_incoming.popleft()
        ordered_nodes.append(node)
        for nextnode in node.outgoing_nodes:
            nextnode.incoming_nodes.remove(node)  # Remove the edge
            if not nextnode.incoming_nodes:  # If no other incoming edges
                zero_incoming.append(nextnode)

    return ordered_nodes