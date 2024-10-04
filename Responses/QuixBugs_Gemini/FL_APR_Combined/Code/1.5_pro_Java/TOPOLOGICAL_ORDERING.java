package java_programs;
        import java.util.*;

        public class TOPOLOGICAL_ORDERING {
            public static ArrayList<Node> topological_ordering (List<Node> directedGraph) {
                ArrayList<Node> orderedNodes = new ArrayList<Node>();
                // Find all nodes with no incoming edges
                for (Node node : directedGraph) {
                    if (node.getPredecessors().isEmpty()) {
                        orderedNodes.add(node);
                    }
                }

                int i = 0;
                // Iterate through the ordered nodes to process their successors
                while (i < orderedNodes.size()) { 
                    Node node = orderedNodes.get(i);
                    // Remove the current node from the predecessors of its successors
                    for (Node nextNode : node.getSuccessors()) {
                        nextNode.getPredecessors().remove(node); 
                        // If a successor has no more predecessors, add it to the ordered list
                        if (nextNode.getPredecessors().isEmpty()) {
                            orderedNodes.add(nextNode); 
                        }
                    }
                    i++; 
                }
                return orderedNodes;
            }
        }
