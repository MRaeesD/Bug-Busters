if node, nextnode in length_by_edge:
    insert_or_update(unvisited_nodes,
                (min(
                    get(unvisited_nodes, nextnode) or float('inf'),
                    get(unvisited_nodes, nextnode) + length_by_edge[node, nextnode]
                ),
                nextnode)
            )
