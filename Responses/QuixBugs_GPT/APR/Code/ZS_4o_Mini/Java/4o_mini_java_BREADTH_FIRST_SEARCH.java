java
package java_programs;
import java.util.*;
import java.util.ArrayDeque;

public class BREADTH_FIRST_SEARCH {

    public static Set<Node> nodesvisited = new HashSet<>();

    public static boolean breadth_first_search(Node startnode, Node goalnode) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.addLast(startnode);

        nodesvisited.add(startnode);

        while (!queue.isEmpty()) { // Changed this line to check for an empty queue
            Node node = queue.removeFirst();

            if (node == goalnode) {
                return true;
            } else {
                for (Node successor_node : node.getSuccessors()) {
                    if (!nodesvisited.contains(successor_node)) {
                        queue.addLast(successor_node); // Changed to addLast for correct BFS behavior
                        nodesvisited.add(successor_node);
                    }
                }
            }
        }
        return false; // Added to return false if goal node is not found
    }

}
