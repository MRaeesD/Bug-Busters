if set(ordered_nodes).issuperset(nextnode.outgoing_nodes) and nextnode not in ordered_nodes:
    # Changed "issuperset" to "issubset" 
    if set(ordered_nodes).issubset(nextnode.outgoing_nodes) and nextnode not in ordered_nodes:
        ordered_nodes.append(nextnode)
