package java_programs;
import java.util.*;

public class DETECT_CYCLE {
    public static boolean detect_cycle(Node node) {
        Node hare = node;
        Node tortoise = node;

        while (true) {
            // Check if hare or tortoise is null before accessing successors
            if (hare == null || hare.getSuccessor() == null) 
                return false;

            tortoise = tortoise.getSuccessor();
            hare = hare.getSuccessor().getSuccessor();

            if (hare == tortoise)
                return true;
        }
    }
}
