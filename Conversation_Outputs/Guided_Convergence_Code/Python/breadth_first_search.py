from collections import deque as Queue

def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:  # Fixed infinite loop by checking if queue is not empty
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            for successor in node.successors:  # Iterate over successors
                if successor not in nodesseen:  # Ensure each node is processed only once
                    queue.append(successor)
                    nodesseen.add(successor)

    return False