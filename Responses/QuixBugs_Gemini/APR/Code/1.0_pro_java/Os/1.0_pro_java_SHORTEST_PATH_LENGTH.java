for (Node nextnode : node.getSuccessors()) {
                    if (visitedNodes.contains(nextnode)) {
                        continue;
                    }

                    if (unvisitedNodes.get(nextnode) == null) {
                        unvisitedNodes.put(nextnode, Integer.MAX_VALUE);
                    }

                    // Change starts here
                    unvisitedNodes.put(nextnode, Math.min(unvisitedNodes.get(nextnode), distance + length_by_edge.get(Arrays.asList(node, nextnode))));
                    // Change ends here
                }
