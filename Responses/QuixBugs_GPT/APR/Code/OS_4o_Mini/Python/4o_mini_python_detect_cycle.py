def detect_cycle(node):
    hare = tortoise = node

    while True:
        if hare is None or hare.successor is None:  # Changed condition here
            return False

        tortoise = tortoise.successor
        hare = hare.successor.successor

        if hare is tortoise:
            return True
