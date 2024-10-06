package java_programs;
import java.util.*;
import java.util.ArrayDeque;

public class BREADTH_FIRST_SEARCH {

    public static boolean breadth_first_search(Node startnode, Node goalnode) {
        Set<Node> nodesvisited = new HashSet<>();
        Deque<Node> queue = new ArrayDeque<>();
        queue.addLast(startnode);

        nodesvisited.add(startnode);

        while (!queue.isEmpty()) {
            Node node = queue.removeFirst();

            if (node.equals(goalnode)) {
                return true;
            } else {
                for (Node successor_node : node.getSuccessors()) {
                    if (!nodesvisited.contains(successor_node)) {
                        queue.addLast(successor_node);
                        nodesvisited.add(successor_node);
                    }
                }
            }
        }
        return false;
    }
}