package java_programs;
import java.util.*;

public class DEPTH_FIRST_SEARCH {
    public static boolean depth_first_search(Node startnode, Node goalnode) {
        // Handle the case of an empty graph
        if (startnode == null) {
            return false; 
        }

        Set<Node> nodesvisited = new HashSet<>();
        class Search {
            boolean search(Node node) {
                // Check if the current node has already been visited
                if (nodesvisited.contains(node)) {
                    return false;
                } 
                // Check if the current node is the goal node
                else if (node == goalnode) {
                    return true;
                } 
                else {
                    // Mark the current node as visited
                    nodesvisited.add(node); 
                    // Recursively search each successor
                    for (Node successornodes : node.getSuccessors()) {
                        if (search(successornodes)) { 
                            return true; 
                        }
                    }
                }
                // Return false if goal node is not found in this path
                return false;
            }
        };

        Search s = new Search();
        return s.search(startnode);
    }
}