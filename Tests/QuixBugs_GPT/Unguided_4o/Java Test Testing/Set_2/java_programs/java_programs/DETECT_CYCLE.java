package java_programs;
import java.util.*;

/* 
class Node {
    private Node successor;

    // Constructor and other methods for Node should be defined here

    public Node getSuccessor() {
        return successor;
    }
}
*/

public class DETECT_CYCLE {
    public static boolean detect_cycle(Node node) {
        Node hare = node;
        Node tortoise = node;

        while (hare != null && hare.getSuccessor() != null) {
            tortoise = tortoise.getSuccessor();
            hare = hare.getSuccessor().getSuccessor();

            if (hare == tortoise)
                return true;
        }

        return false;
    }
}