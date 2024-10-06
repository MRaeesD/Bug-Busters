package java_programs;
import java.util.*;
public class KTH {
    public static Integer kth(ArrayList<Integer> arr, int k) {
        if (arr.isEmpty()) {
            throw new IllegalArgumentException("Array cannot be empty");
        }
        int pivot = arr.get(0);
        ArrayList<Integer> below, above;
        below = new ArrayList<Integer>(arr.size());
        above = new ArrayList<Integer>(arr.size());
        ArrayList<Integer> pivots = new ArrayList<Integer>(arr.size()); // added to store pivots
        
        for (Integer x : arr) {
            if (x < pivot) {
                below.add(x);
            } else if (x > pivot) {
                above.add(x);
            } else {
                pivots.add(x); // collect pivot occurrences
            }
        }
        
        int num_less = below.size();
        int num_lessoreq = num_less + pivots.size(); // changed to include pivots

        if (k < num_less) {
            return kth(below, k);
        } else if (k >= num_lessoreq) {
            return kth(above, k - num_lessoreq); // adjusted 'k' to account for 'num_lessoreq'
        } else {
            return pivot;
        }
    }
}