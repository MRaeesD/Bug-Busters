def detect_cycle(node):
    if node is None:  # Bug: Missing null check for input node
        return False
    hare = tortoise = node

    while hare is not None and hare.successor is not None:  # Bug: Potential infinite loop
        tortoise = tortoise.successor
        hare = hare.successor.successor

        if hare is tortoise:
            return True

    return False  # No cycle found