class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def minimum_spanning_tree(weight_by_edge):
    nodes = set()
    for u, v in weight_by_edge:
        nodes.add(u)
        nodes.add(v)
    
    uf = UnionFind(len(nodes))
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.get):
        u, v = edge
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.add(edge)

    return mst_edges