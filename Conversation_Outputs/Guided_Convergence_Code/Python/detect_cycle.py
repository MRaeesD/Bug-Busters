def detect_cycle(node):
    hare = tortoise = node

    while True:
        # The bug is addressed here. We need to ensure both hare and hare.successor are not None
        # before advancing the hare pointer two steps.
        if hare is None or hare.successor is None:
            return False

        tortoise = tortoise.successor
        hare = hare.successor.successor

        if hare is tortoise:
            return True