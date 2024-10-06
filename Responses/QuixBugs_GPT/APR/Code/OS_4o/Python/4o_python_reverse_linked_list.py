def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node  # This line was omitted and is now added
        node = nextnode
    return prevnode
