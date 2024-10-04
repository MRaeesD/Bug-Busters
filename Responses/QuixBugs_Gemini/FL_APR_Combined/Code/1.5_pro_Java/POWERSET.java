package java_programs;
    import java.util.*;
    
    
    public class POWERSET {
        public static ArrayList<ArrayList<Object>> powerset(ArrayList<Object> arr) {
            if (!arr.isEmpty()) {
                Object first = arr.get(0);
                arr.remove(0);
                ArrayList<Object> rest = new ArrayList<>(arr); // Create a copy of 'rest' to avoid modifying the original 'arr'
                ArrayList<ArrayList<Object>> rest_subsets = powerset(rest);
    
                ArrayList<ArrayList<Object>> output = new ArrayList<ArrayList<Object>>(); // Initialize 'output' without a fixed capacity
                for (ArrayList<Object> subset : rest_subsets) {
                    ArrayList<Object> newSubset = new ArrayList<Object>(subset); // Create a new ArrayList for each subset
                    newSubset.add(first); // Add 'first' to the new subset
                    output.add(newSubset); // Add the new subset to 'output'
                }
                output.addAll(rest_subsets); // Add all subsets from 'rest_subsets' to 'output'
    
                return output;
            } else {
                ArrayList<ArrayList<Object>> empty_set = new ArrayList<ArrayList<Object>>(); // Initialize 'empty_set' as an ArrayList of ArrayLists
                empty_set.add(new ArrayList<Object>()); // Add an empty ArrayList to represent the empty set
                return empty_set;
            }
        }
    }
