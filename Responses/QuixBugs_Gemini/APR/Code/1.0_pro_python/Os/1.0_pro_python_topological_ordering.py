if set(ordered_nodes).issubset(nextnode.outgoing_nodes) and nextnode not in ordered_nodes:
                
                ordered_nodes.append(nextnode)
