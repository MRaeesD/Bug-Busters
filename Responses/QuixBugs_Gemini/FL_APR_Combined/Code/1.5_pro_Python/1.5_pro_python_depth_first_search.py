def depth_first_search(startnode, goalnode):
        # Move nodesvisited inside the search_from function
        nodesvisited = set()  

        def search_from(node):
            if node in nodesvisited:
                return False
            # Use == for node comparison for safety 
            elif node == goalnode: 
                return True
            else:
                nodesvisited.add(node)  # Mark the node as visited
                return any(
                    search_from(nextnode) for nextnode in node.successors
                )

        return search_from(startnode)
