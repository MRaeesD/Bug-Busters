def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node  # Update prevnode before moving to the next node
        node = nextnode
    return prevnode
