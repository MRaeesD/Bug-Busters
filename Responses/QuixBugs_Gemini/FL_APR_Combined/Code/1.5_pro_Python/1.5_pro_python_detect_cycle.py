def detect_cycle(node):
    hare = tortoise = node

    while True:
        # Fix: Check if hare.successor.successor is None to avoid AttributeError
        if hare is None or hare.successor is None: 
            return False

        tortoise = tortoise.successor
        hare = hare.successor.successor

        if hare is tortoise:
            return True
