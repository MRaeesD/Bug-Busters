def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        # Assign the current node to prevnode
        prevnode = node
        node.successor = prevnode
        node = nextnode
    return prevnode
