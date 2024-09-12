def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        if group_by_node.setdefault(u, {u}) != group_by_node.setdefault(v, {v}):
            mst_edges.add(edge)
            group_by_node[u].update(group_by_node[v])
            # Change: Only update the groups of the nodes in v if they are not already in u's group
            for node in group_by_node[v]:
                if node not in group_by_node[u]:
                    group_by_node[node].update(group_by_node[u])

    return mst_edges
