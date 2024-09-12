def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor  # Store the next node.
        node.successor = prevnode  # Link the current node to the previous node.
        prevnode = node  # Update the previous node.
        node = nextnode  # Move to the next node.
    return prevnode
