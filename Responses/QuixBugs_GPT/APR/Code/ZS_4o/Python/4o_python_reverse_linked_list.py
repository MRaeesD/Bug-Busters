def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        currentnode = node  # Correct placement of line
        node.successor = prevnode
        prevnode = currentnode  # Ensuring the loop progresses correctly
        node = nextnode
    return prevnode
