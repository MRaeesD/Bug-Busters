class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self._successor = successor  # Changed attribute name
        self._successors = successors  # Changed attribute name
        self._predecessors = predecessors  # Changed attribute name
        self.incoming_nodes = incoming_nodes
        self.outgoing_nodes = outgoing_nodes

    def get_successor(self):  # Changed method name
        return self._successor

    def get_successors(self):  # Changed method name
        return self._successors

    def get_predecessors(self):  # Changed method name
        return self._predecessors
