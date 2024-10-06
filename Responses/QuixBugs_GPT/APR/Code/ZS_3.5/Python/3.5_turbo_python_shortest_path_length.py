(min(
                    get(unvisited_nodes, nextnode) or float('inf'),
                    distance + length_by_edge[node, nextnode]
                ),
