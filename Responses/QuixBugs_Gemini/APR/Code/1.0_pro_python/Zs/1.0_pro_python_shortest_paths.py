weight_by_edge[u, v] = min(
                weight_by_node[u] + weight,
                weight_by_node[v] + weight
            ) # Change made here
