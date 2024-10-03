def reverse_linked_list(node):
        prevnode = None
        while node:
            nextnode = node.next  # Fix: Changed 'successor' to 'next'
            node.next = prevnode  # Fix: Changed 'successor' to 'next'
            node = nextnode
        return prevnode
