package java_programs;
import java.util.*;

import java_programs.Node;

public class DETECT_CYCLE {
    public static boolean detect_cycle(Node node) {
        Node hare = node;
        Node tortoise = node;

        while (true) {
            if (hare.getSuccessor() == null) 
                return false;

            tortoise = tortoise.getSuccessor();
            if (hare.getSuccessor() == null || hare.getSuccessor().getSuccessor() == null) // Check if either hare.getSuccessor() or hare.getSuccessor().getSuccessor() is null
                return false;
            hare = hare.getSuccessor().getSuccessor(); 

            if (hare == tortoise)
                return true;
        }
    }
}