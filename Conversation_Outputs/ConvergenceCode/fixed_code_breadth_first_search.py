from collections import deque as Queue

def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:  # Check if the queue is not empty
        node = queue.popleft()

        if node == goalnode:  # Use equality check instead of identity check
            return True
        else:
            for successor in node.successors:
                if successor not in nodesseen:  # Check if successor has been seen before
                    queue.append(successor)
                    nodesseen.add(successor)  # Update nodesseen immediately

    return False