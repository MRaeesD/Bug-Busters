def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor  # save the successor
        node.successor = prevnode   # change the successor
        prevnode = node            # update prevnode to current
        node = nextnode
    return prevnode
