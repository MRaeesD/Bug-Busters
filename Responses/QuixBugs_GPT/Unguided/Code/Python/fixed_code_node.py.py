class Node:
    def __init__(self, value=None, successor=None, successors=None, predecessors=None, incoming_nodes=None, outgoing_nodes=None):
        self.value = value
        self.successor = successor
        self.successors = successors if successors is not None else []
        self.predecessors = predecessors if predecessors is not None else []
        self.incoming_nodes = incoming_nodes if incoming_nodes is not None else []
        self.outgoing_nodes = outgoing_nodes if outgoing_nodes is not None else []

    def get_successor(self):
        return self.successor

    def get_successors(self):
        return self.successors

    def get_predecessors(self):
        return self.predecessors