def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        prevnode = node # <-- The missing line
        node.successor = prevnode
        node = nextnode
    return prevnode
