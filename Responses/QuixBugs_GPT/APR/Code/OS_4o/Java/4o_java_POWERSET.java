package java_programs;
import java.util.*;

public class POWERSET {
    public static ArrayList<ArrayList> powerset(ArrayList arr) {
        if (!arr.isEmpty()) {
            Object first = arr.get(0);
            arr.remove(0);
            ArrayList rest = new ArrayList(arr); // Copy the rest to avoid altering original array
            ArrayList<ArrayList> rest_subsets = powerset(rest);

            ArrayList<ArrayList> output = new ArrayList<ArrayList>();
            for (ArrayList subset : rest_subsets) { // Corrected loop handling
                ArrayList new_subset = new ArrayList(subset);
                new_subset.add(first);
                output.add(new_subset);
            }
            output.addAll(rest_subsets); // Add all subsets generated from rest
            return output;
        } else {
            ArrayList<ArrayList> empty_set = new ArrayList<>();
            empty_set.add(new ArrayList());
            return empty_set;
        }
    }
}
