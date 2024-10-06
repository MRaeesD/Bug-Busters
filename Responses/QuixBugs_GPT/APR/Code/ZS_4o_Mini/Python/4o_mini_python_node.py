class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self._successor = successor  # Changed to _successor to avoid conflict
        self._successors = successors  # Changed to _successors to avoid conflict
        self._predecessors = predecessors  # Changed to _predecessors to avoid conflict
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def successor(self):
        return self._successor  # Referenced _successor instead of successor

    def successors(self):
        return self._successors  # Referenced _successors instead of successors

    def predecessors(self):
        return self._predecessors  # Referenced _predecessors instead of predecessors
