} else {
                nodesvisited.add(node); // <-- Added this line to mark the current node as visited
                for (Node successornodes : node.getSuccessors()) {
                    if (search(successornodes)) { return true; }
                }
            }
