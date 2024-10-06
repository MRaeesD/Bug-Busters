class Node:
    def __init__(self, value=None, successor=None, successors=[], predecessors=[], incoming_nodes=[], outgoing_nodes=[]):
        self.value = value
        self.success = successor
        self.successors_list = successors
        self.predecessors_list = predecessors
        self.incoming_nodes_list = incoming_nodes
        self.outgoing_nodes_list = outgoing_nodes

    def get_successor(self):
        return self.success

    def get_successors(self):
        return self.successors_list

    def get_predecessors(self):
        return self.predecessors_list
