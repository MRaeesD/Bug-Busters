class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self._successor = successor  # Changed from self.successor to self._successor
        self._successors = successors  # Changed from self.successors to self._successors
        self._predecessors = predecessors  # Changed from self.predecessors to self._predecessors
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def successor(self):
        return self._successor  # Updated to return self._successor

    def successors(self):
        return self._successors  # Updated to return self._successors

    def predecessors(self):
        return self._predecessors  # Updated to return self._predecessors
