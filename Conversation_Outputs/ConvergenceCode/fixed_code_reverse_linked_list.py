def reverse_linked_list(node):
    prevnode = None  # Fixed Indentation Error
    while node:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node  # Fixed Missing Update of `prevnode`
        node = nextnode
    return prevnode