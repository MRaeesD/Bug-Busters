from collections import deque

class OrderedSet:
    def __init__(self):
        self.items = []
        self.set_items = set()
    
    def append(self, item):
        if item not in self.set_items:
            self.items.append(item)
            self.set_items.add(item)

    def __iter__(self):
        return iter(self.items)

def topological_ordering(nodes):
    ordered_nodes = OrderedSet()
    no_incoming = deque([node for node in nodes if not node.incoming_nodes])
    
    while no_incoming:
        node = no_incoming.popleft()
        ordered_nodes.append(node)
        
        for nextnode in node.outgoing_nodes:
            nextnode.incoming_nodes.remove(node)
            if not nextnode.incoming_nodes:
                no_incoming.append(nextnode)
    
    return ordered_nodes
