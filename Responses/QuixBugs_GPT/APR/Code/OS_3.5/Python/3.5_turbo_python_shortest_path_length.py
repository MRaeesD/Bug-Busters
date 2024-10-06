def insert_or_update(node_heap, dist_node):
    dist, node = dist_node
    for i, tpl in enumerate(node_heap):
        a, b = tpl
        if b == node:
            node_heap[i] = dist_node  # heapq retains sorted property
            return None

    current_dist = get(node_heap, node)  # Get the current distance to the node
    new_dist = min(current_dist, dist)
    node_heap.append((new_dist, node))
    heapify(node_heap)  # Re-heapify to maintain the heap property
    return None
