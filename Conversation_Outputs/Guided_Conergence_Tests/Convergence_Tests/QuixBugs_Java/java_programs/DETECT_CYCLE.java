package java_programs;
import java.util.*;

public class DETECT_CYCLE {
    public static boolean detect_cycle(Node node) {
        // If the list is empty, there's no cycle
        if (node == null) return false; 

        Node hare = node;
        Node tortoise = node;

        while (true) {
            // Check if hare or hare's successor is null to avoid NullPointerException
            if (hare == null || hare.getSuccessor() == null) // Bug fix: Added check for hare == null
                return false;

            // Move tortoise one step
            tortoise = tortoise.getSuccessor();
            // Move hare two steps
            hare = hare.getSuccessor().getSuccessor();

            // If hare and tortoise meet, there's a cycle
            if (hare == tortoise)
                return true;
        }
    }
}