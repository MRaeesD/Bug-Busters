def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])  # Path compression
    return parent[node]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def minimum_spanning_tree(weight_by_edge):
    parent = {}
    rank = {}
    mst_edges = set()

    for edge in weight_by_edge:
        u, v = edge
        parent[u] = u
        parent[v] = v
        rank[u] = 0
        rank[v] = 0

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        if find(parent, u) != find(parent, v):
            mst_edges.add(edge)
            union(parent, rank, u, v)

    return mst_edges