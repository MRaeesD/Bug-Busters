nextnode = node.successor #Declare successor node
        node.successor = prevnode #Set current node's successor to previous node
        prevnode = node #Set previous node to current node
        node = nextnode #Set current node to successor node
