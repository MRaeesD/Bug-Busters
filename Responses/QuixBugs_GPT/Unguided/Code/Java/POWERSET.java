package java_programs;
import java.util.*;

public class POWERSET {
    public static ArrayList<ArrayList<Object>> powerset(ArrayList<Object> arr) {
        if (!arr.isEmpty()) {
            Object first = arr.get(0);
            ArrayList<Object> rest = new ArrayList<>(arr.subList(1, arr.size()));
            ArrayList<ArrayList<Object>> rest_subsets = powerset(rest);

            ArrayList<ArrayList<Object>> output = new ArrayList<>();
            for (ArrayList<Object> subset : rest_subsets) {
                output.add(new ArrayList<>(subset)); // Add the subset as is
                ArrayList<Object> newSubset = new ArrayList<>(subset); // Create a new subset with 'first' element
                newSubset.add(0, first);
                output.add(newSubset);
            }

            return output;
        } else {
            ArrayList<ArrayList<Object>> empty_set = new ArrayList<>();
            empty_set.add(new ArrayList<>());
            return empty_set;
        }
    }
}