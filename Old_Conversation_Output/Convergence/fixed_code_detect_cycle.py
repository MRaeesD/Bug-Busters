def detect_cycle(node):
    # Initialize hare and tortoise to the head of the linked list
    hare = tortoise = node

    while True:
        # Check if hare's next step is None, indicating no cycle
        # Bug fix: Added check for hare is None to avoid AttributeError 
        if hare is None or hare.successor is None:  
            return False
        
        # Move tortoise one step and hare two steps
        tortoise = tortoise.successor
        # Bug fix: The check above prevents AttributeError here
        hare = hare.successor.successor 
        
        # If hare and tortoise meet, a cycle is detected
        if hare is tortoise:
            return True