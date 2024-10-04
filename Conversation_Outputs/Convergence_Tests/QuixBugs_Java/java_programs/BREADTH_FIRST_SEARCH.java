package java_programs;
import java.util.*;
import java.util.ArrayDeque;
import java_programs.Node;

public class BREADTH_FIRST_SEARCH {

    public static boolean breadth_first_search(Node startnode, Node goalnode) {
        Deque<Node> queue = new ArrayDeque<>();
        Set<Node> nodesvisited = new HashSet<>(); // Local variable to avoid global state issues
        queue.addLast(startnode);
        nodesvisited.add(startnode);

        while (!queue.isEmpty()) { // Termination condition added
            Node node = queue.removeFirst(); // Safe removal due to the loop condition

            if (node.equals(goalnode)) { // Corrected comparison
                return true;
            } else {
                for (Node successor_node : node.getSuccessors()) {
                    if (!nodesvisited.contains(successor_node)) {
                        queue.addLast(successor_node); // Corrected to add to the back of the queue
                        nodesvisited.add(successor_node);
                    }
                }
            }
        }
        return false; // Return false if goal node is not found
    }
}