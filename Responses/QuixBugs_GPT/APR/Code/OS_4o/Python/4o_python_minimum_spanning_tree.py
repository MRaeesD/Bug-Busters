def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        if group_by_node.setdefault(u, {u}) != group_by_node.setdefault(v, {v}):
            mst_edges.add(edge)
            combined_group = group_by_node[u].union(group_by_node[v])
            for node in combined_group:
                group_by_node[node] = combined_group  # change is here

    return mst_edges
