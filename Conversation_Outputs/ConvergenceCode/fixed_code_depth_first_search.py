def depth_first_search(startnode, goalnode):
    nodesvisited = set()  # Fixed indentation issue

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node == goalnode:  # Changed 'is' to '=='
            return True
        else:
            nodesvisited.add(node)  # Update visited nodes
            return any(
                search_from(nextnode) for nextnode in getattr(node, 'successors', [])
            )
    
    return search_from(startnode)