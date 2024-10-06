package java_programs;
import java.util.*;

public class TOPOLOGICAL_ORDERING {
    public static ArrayList<Node> topological_ordering (List<Node> directedGraph) {
        ArrayList<Node> orderedNodes = new ArrayList<Node>();
        
        // Start by adding all nodes with no predecessors
        for (Node node : directedGraph) {
            if (node.getPredecessors().isEmpty()) {
                orderedNodes.add(node);
            }
        }

        int index = 0;
        while (index < orderedNodes.size()) {
            Node node = orderedNodes.get(index);
            for (Node nextNode : node.getSuccessors()) {
                if (orderedNodes.contains(nextNode)) continue;
                
                boolean allPredecessorsAdded = true;
                for (Node predecessor : nextNode.getPredecessors()) {
                    if (!orderedNodes.contains(predecessor)) {
                        allPredecessorsAdded = false;
                        break;
                    }
                }
                
                if (allPredecessorsAdded) {
                    orderedNodes.add(nextNode);
                }
            }
            index++;
        }
        
        return orderedNodes;
    }
}
/* 
class Node {
    private List<Node> successors;
    private List<Node> predecessors;

    public Node() {
        this.successors = new ArrayList<>();
        this.predecessors = new ArrayList<>();
    }

    public List<Node> getSuccessors() {
        return successors;
    }

    public List<Node> getPredecessors() {
        return predecessors;
    }
    
    public void addSuccessor(Node successor) {
        this.successors.add(successor);
    }

    public void addPredecessor(Node predecessor) {
        this.predecessors.add(predecessor);
    }
}
*/