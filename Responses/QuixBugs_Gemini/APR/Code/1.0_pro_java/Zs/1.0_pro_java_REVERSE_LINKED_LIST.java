while (node != null) {
            nextnode = node.getSuccessor(); // Store the next node
            node.setSuccessor(prevnode); // Update the successor of the current node to point to the previous node
            node = nextnode; // Advance the current node to the next node
        }
        return prevnode;
    }
