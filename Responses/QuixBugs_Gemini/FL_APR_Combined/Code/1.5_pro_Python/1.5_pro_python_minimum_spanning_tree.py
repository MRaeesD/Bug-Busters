def minimum_spanning_tree(weight_by_edge):
        group_by_node = {}
        mst_edges = set()

        for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
            u, v = edge
            if group_by_node.setdefault(u, {u}) != group_by_node.setdefault(v, {v}):
                mst_edges.add(edge)
                # Fix: Update all nodes in the merged set after merging
                group_u = group_by_node[u] 
                group_v = group_by_node[v]
                for node in group_u | group_v:
                    group_by_node[node] = group_u | group_v

        return mst_edges
