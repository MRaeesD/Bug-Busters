package java_programs;
import java.util.*;

/* 
class Node {
    private Node successor;

    public Node getSuccessor() {
        return successor;
    }

    public void setSuccessor(Node successor) {
        this.successor = successor;
    }

    // Assume there are other necessary methods and properties
}
*/
public class REVERSE_LINKED_LIST {
    public static Node reverse_linked_list(Node node) {
        Node prevnode = null;
        Node nextnode = null;
        while (node != null) {
            nextnode = node.getSuccessor();
            node.setSuccessor(prevnode);
            prevnode = node;  // This step was missing and is necessary to traverse correctly
            node = nextnode;
        }
        return prevnode;
    }
}