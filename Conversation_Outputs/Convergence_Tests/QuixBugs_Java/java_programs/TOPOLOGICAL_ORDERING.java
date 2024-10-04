package java_programs;

import java.util.*;

public class TOPOLOGICAL_ORDERING {
    public static ArrayList<Node> topological_ordering(List<Node> directedGraph) {
        ArrayList<Node> orderedNodes = new ArrayList<Node>();
        Queue<Node> processQueue = new LinkedList<Node>();

        // Initialize the queue with nodes having no predecessors
        for (Node node : directedGraph) {
            if (node.getPredecessors().isEmpty()) {
                processQueue.add(node);
            }
        }

        while (!processQueue.isEmpty()) {
            Node node = processQueue.poll();
            orderedNodes.add(node);

            for (Node nextNode : node.getSuccessors()) {
                // Check if all predecessors of the nextNode are in orderedNodes
                boolean allPredecessorsProcessed = true;
                for (Node predecessor : nextNode.getPredecessors()) {
                    if (!orderedNodes.contains(predecessor)) {
                        allPredecessorsProcessed = false;
                        break;
                    }
                }
                // Add the node to the queue if all predecessors are processed
                if (allPredecessorsProcessed && !orderedNodes.contains(nextNode)) {
                    processQueue.add(nextNode);
                }
            }
        }
        return orderedNodes;
    }
}