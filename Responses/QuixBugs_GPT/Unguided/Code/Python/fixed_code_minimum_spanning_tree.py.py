def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    # Sort edges based on weight
    for edge in sorted(weight_by_edge, key=weight_by_edge.get):
        u, v = edge
        group_u = find(group_by_node, u)
        group_v = find(group_by_node, v)

        # Check if the nodes u and v are in different groups
        if group_u != group_v:
            mst_edges.add(edge)
            union(group_by_node, group_u, group_v)

    return mst_edges

def find(group_by_node, node):
    if group_by_node.setdefault(node, node) != node:
        group_by_node[node] = find(group_by_node, group_by_node[node])
    return group_by_node[node]

def union(group_by_node, group_u, group_v):
    group_by_node[group_v] = group_u
