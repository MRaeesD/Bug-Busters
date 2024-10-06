def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        if group_by_node.setdefault(u, {u}) != group_by_node.setdefault(v, {v}):
            mst_edges.add(edge)
            old_group = group_by_node[v]  # Change here: store the old group
            new_group = group_by_node[u]
            new_group.update(old_group)
            for node in old_group:
                group_by_node[node] = new_group  # Change here: properly update reference

    return mst_edges
