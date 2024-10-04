package java_programs;
import java.util.*;

public class KTH {
    public static Integer kth(ArrayList<Integer> arr, int k) {
        int pivot = arr.get(0);
        ArrayList<Integer> below, above;
        below = new ArrayList<>(arr.size());
        above = new ArrayList<>(arr.size());

        for (Integer x : arr) {
            if (x < pivot) {
                below.add(x);
            } else if (x > pivot) {
                above.add(x);
            } 
        }
        // FIX: Add the pivot to 'below' to ensure it's included in the partitioning.
        below.add(pivot); 

        int num_less = below.size();
        int num_lessoreq = num_less; // Pivot is now included in 'below'

        if (k < num_less) {
            return kth(below, k);
        } else if (k >= num_lessoreq) {
            // FIX: Adjust 'k' when recursing on 'above' to maintain the correct index.
            return kth(above, k - num_lessoreq); 
        } else {
            return pivot;
        }
    }
}