class Node:
    def __init__(self, value=None, successors=None, predecessors=None, incoming_nodes=None, outgoing_nodes=None):
        self.value = value
        self.successors = successors if successors is not None else []  # Fixed mutable default argument
        self.predecessors = predecessors if predecessors is not None else []  # Fixed mutable default argument
        self.incoming_nodes = incoming_nodes if incoming_nodes is not None else []  # Fixed mutable default argument
        self.outgoing_nodes = outgoing_nodes if outgoing_nodes is not None else []  # Fixed mutable default argument

    def get_successors(self):
        return self.successors  # Renamed method to avoid conflict

    def get_predecessors(self):
        return self.predecessors  # Renamed method to avoid conflict