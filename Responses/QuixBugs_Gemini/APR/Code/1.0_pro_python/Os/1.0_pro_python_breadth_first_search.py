while queue:  # Line changed
    node = queue.popleft()

    if node is goalnode:
        return True
    else:
        queue.extend(node for node in node.successors if node not in nodesseen)
        nodesseen.update(node.successors)

return False
