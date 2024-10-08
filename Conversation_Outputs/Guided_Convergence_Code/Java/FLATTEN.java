package java_programs;
import java.util.*;

/**
 * Flattens a nested list structure into a single list of elements.
 * 
 * @param arr The input object, expected to be a List or a single non-list element.
 * @return A flattened List of elements.
 * @throws IllegalArgumentException if the input is null or not a List or non-list object.
 */
public class FLATTEN {
    public static <T> List<T> flatten(Object arr) {
        if (arr == null) {
            throw new IllegalArgumentException("Input cannot be null");
        }
        
        if (arr instanceof List<?>) { 
            List<?> narr = (List<?>) arr;
            List<T> result = new ArrayList<>(); 
            for (Object x : narr) {
                if (x instanceof List) {
                    result.addAll(flatten((List<?>) x)); 
                } else {
                    result.add((T) x); 
                }
            }
            return result;
        } else if (arr instanceof Object) {
            return Collections.singletonList((T) arr);
        } else {
            throw new IllegalArgumentException("Unsupported input type");
        }
    }
}