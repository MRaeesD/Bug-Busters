for (Node nextnode : node.getSuccessors()) {
                    if (visitedNodes.contains(nextnode)) {
                        continue;
                    }

                    if (unvisitedNodes.get(nextnode) == null) {
                        unvisitedNodes.put(nextnode, Integer.MAX_VALUE);
                    }

                    // Change made here. Added the distance between the current node and the next node to the current distance of the next node.
                    unvisitedNodes.put(nextnode, Math.min(unvisitedNodes.get(nextnode), unvisitedNodes.get(node) + length_by_edge.get(Arrays.asList(node, nextnode))));
                }
