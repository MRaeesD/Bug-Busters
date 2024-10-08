package java_programs;
import java.util.*;


public class POWERSET {
    public static ArrayList<ArrayList> powerset(ArrayList arr) {
        if (!arr.isEmpty()) {
            Object first = arr.get(0);
            arr.remove(0);
            ArrayList rest = arr;
            ArrayList<ArrayList> rest_subsets = powerset(rest);

            ArrayList<ArrayList> output = new ArrayList<ArrayList>();
            output.addAll(rest_subsets); // Add all subsets of the rest of the array

            // Iterate through the subsets of the rest of the array
            for (ArrayList subset : rest_subsets) {
                ArrayList new_subset = new ArrayList(subset); // Create a new subset
                new_subset.add(0, first); // Add the first element to the new subset
                output.add(new_subset); // Add the new subset to the output array
            }

            return output;
        } else {
            ArrayList empty_set = new ArrayList<ArrayList>();
            empty_set.add(new ArrayList());
            return empty_set;
        }
    }
}