class Node:
    def __init__(self, value=None, successor=None, successors=None, predecessors=None, incoming_nodes=None, outgoing_nodes=None):
        self.value = value
        self.successor = successor
        self.successors = successors if successors is not None else []  # Changed to handle mutable default arguments
        self.predecessors = predecessors if predecessors is not None else []  # Changed to handle mutable default arguments
        self.incoming_nodes = incoming_nodes if incoming_nodes is not None else []  # Changed to handle mutable default arguments
        self.outgoing_nodes = outgoing_nodes if outgoing_nodes is not None else []  # Changed to handle mutable default arguments

    def get_successor(self):  # Method name changed to avoid conflict with attribute
        return self.successor

    def get_successors(self):  # Method name changed to avoid conflict with attribute
        return self.successors

    def get_predecessors(self):  # Method name changed to avoid conflict with attribute
        return self.predecessors
