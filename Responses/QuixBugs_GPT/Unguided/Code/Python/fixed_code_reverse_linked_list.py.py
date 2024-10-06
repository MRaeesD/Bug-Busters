def reverse_linked_list(node):
    prevnode = None
    current = node
    while current:
        nextnode = current.successor
        current.successor = prevnode
        prevnode = current
        current = nextnode
    return prevnode