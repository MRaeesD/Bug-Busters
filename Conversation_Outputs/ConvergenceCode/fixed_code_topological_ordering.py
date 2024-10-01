from collections import deque

def topological_ordering(nodes):
    """
    Performs a topological sort of the given nodes using Kahn's algorithm.
    """
    ordered_nodes = []
    zero_incoming = deque([node for node in nodes if not node.incoming_nodes])

    while zero_incoming:
        node = zero_incoming.popleft()
        ordered_nodes.append(node)
        for nextnode in node.outgoing_nodes:
            nextnode.incoming_nodes.remove(node)
            if not nextnode.incoming_nodes:  # Bug fixed: Correctly managing incoming nodes
                zero_incoming.append(nextnode)

    return ordered_nodes