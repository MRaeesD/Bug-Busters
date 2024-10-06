unvisitedNodes.put(nextnode, Math.min(unvisitedNodes.get(nextnode),
                        distance + length_by_edge.get(Arrays.asList(node, nextnode))));
