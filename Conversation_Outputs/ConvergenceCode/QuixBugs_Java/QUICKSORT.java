package java_programs;
import java.util.*;

public class QUICKSORT {
    public static ArrayList<Integer> quicksort(ArrayList<Integer> arr) {
        if (arr.isEmpty()) {
            return new ArrayList<Integer>();
        }

        Integer pivot = arr.get(0);
        ArrayList<Integer> lesser = new ArrayList<Integer>();
        ArrayList<Integer> greater = new ArrayList<Integer>();
        ArrayList<Integer> equal = new ArrayList<Integer>(); // Separate list for duplicates

        for (Integer x : arr) {  // Include the pivot in the loop
            if (x < pivot) {
                lesser.add(x);
            } else if (x > pivot) {
                greater.add(x);
            } else {
                equal.add(x); // Add elements equal to the pivot
            }
        }
        
        lesser = quicksort(lesser);
        greater = quicksort(greater);
        
        // Correct merge order: lesser + equal + greater
        lesser.addAll(equal); // Add equal elements to lesser
        lesser.addAll(greater); // Then add greater elements
        
        return lesser;
    }
}