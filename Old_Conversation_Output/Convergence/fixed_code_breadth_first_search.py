from collections import deque as Queue

def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    # BUG: Missing `queue.empty()` Check - The loop needs a condition to terminate if the goal node is not found.
    while True: 
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            # BUG: Incorrect `nodesseen` Update -  `nodesseen` should be updated with each successor right *before* it's added to the queue.
            queue.extend(node for node in node.successors if node not in nodesseen)
            nodesseen.update(node.successors)

    return False