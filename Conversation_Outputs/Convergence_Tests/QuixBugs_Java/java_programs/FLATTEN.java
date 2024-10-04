package java_programs;
import java.util.*;

public class FLATTEN {
    public static Object flatten(Object arr) {
        if (arr instanceof List) { // Use List interface instead of ArrayList
            List narr = (List) arr; // Cast to List
            List result = new ArrayList(); // Use List for result
            for (Object x : narr) {
                if (x instanceof List) {
                    result.addAll((List) flatten(x)); // Cast to List
                } else {
                    result.add(x); // Fix: Directly add the non-list element
                }
            }
            return result;
        } else {
            return arr; // Fix: Base case to return non-list objects
        }
    }
}