class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.successor_node = successor
        self.successor_nodes = successors
        self.predecessor_nodes = predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def get_successor_node(self):
        return self.successor_node

    def get_successor_nodes(self):
        return self.successor_nodes

    def get_predecessor_nodes(self):
        return self.predecessor_nodes
