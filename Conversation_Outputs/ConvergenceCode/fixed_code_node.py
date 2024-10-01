class Node:
    """
    Represents a node in a directed graph.

    Attributes:
        value: The value stored in the node.
        successor: The direct successor node (for linear structures).
        successors: A list of successor nodes in the graph.
        predecessors: A list of predecessor nodes in the graph.
        incoming_nodes: A list of nodes that have an edge directed towards this node.
        outgoing_nodes: A list of nodes that this node has an edge directed towards. 
    """
    def __init__(self, value=None, successor=None, successors=None, predecessors=None, incoming_nodes=None, outgoing_nodes=None):
        self.value = value
        self.successor = successor 
        self.successors = successors if successors is not None else [] 
        self.predecessors = predecessors if predecessors is not None else [] 
        self.incoming_nodes = incoming_nodes if incoming_nodes is not None else []  
        self.outgoing_nodes = outgoing_nodes if outgoing_nodes is not None else [] 

    def get_successor(self):
        """Returns the direct successor node."""
        return self.successor 

    def get_successors(self):
        """Returns a list of all successor nodes."""
        return self.successors 

    def get_predecessors(self):
        """Returns a list of all predecessor nodes."""
        return self.predecessors 