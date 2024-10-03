from collections import deque

    def breadth_first_search(startnode, goalnode):
        # Use deque directly for clarity
        queue = deque()  
        queue.append(startnode)

        nodesseen = set()
        nodesseen.add(startnode)

        while queue:  # Check if queue is not empty
            node = queue.popleft()

            if node is goalnode:
                return True

            # Iterate through successors and add unseen nodes to the queue
            for successor in node.successors:
                if successor not in nodesseen:
                    nodesseen.add(successor)  # Mark as seen immediately
                    queue.append(successor)

        return False  # Goal node not found
