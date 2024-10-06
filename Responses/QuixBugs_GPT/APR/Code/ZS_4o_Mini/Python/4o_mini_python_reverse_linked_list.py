def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        node.successor = prevnode  # The line assigns the previous node to the current node's successor
        prevnode = node  # This line was added to update prevnode to the current node
        node = nextnode
    return prevnode
