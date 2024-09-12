def detect_cycle(node):
    hare = tortoise = node

    while True:
        # Change is here:
        if hare is None: 
            return False

        tortoise = tortoise.successor
        hare = hare.successor.successor

        if hare is tortoise:
            return True
