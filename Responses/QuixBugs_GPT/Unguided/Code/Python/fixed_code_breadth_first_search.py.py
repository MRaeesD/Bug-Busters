from collections import deque as Queue

def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:
        node = queue.popleft()

        if node == goalnode:
            return True
        else:
            new_successors = [succ for succ in node.successors if succ not in nodesseen]
            queue.extend(new_successors)
            nodesseen.update(new_successors)

    return False