package java_programs;
    import java.util.*;
    
    public class DETECT_CYCLE {
        public static boolean detect_cycle(Node node) {
            Node hare = node;
            Node tortoise = node;
    
            while (true) {
                if (hare.getSuccessor() == null || hare.getSuccessor().getSuccessor() == null) // Bug fix: Check if hare or hare's successor is null
                    return false;
    
                tortoise = tortoise.getSuccessor();
                hare = hare.getSuccessor().getSuccessor();
    
                if (hare == tortoise)
                    return true;
            }
        }
    }
