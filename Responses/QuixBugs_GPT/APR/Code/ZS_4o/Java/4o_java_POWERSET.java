package java_programs;
import java.util.*;

public class POWERSET {
    public static ArrayList<ArrayList> powerset(ArrayList arr) {
        if (!arr.isEmpty()) { 
            Object first = arr.get(0); 
            arr.remove(0); 
            ArrayList rest = new ArrayList(arr); // Corrected line to ensure 'rest' has elements of 'arr'
            ArrayList<ArrayList> rest_subsets = powerset(rest); 

            ArrayList<ArrayList> output = new ArrayList<ArrayList>(); // Corrected initialization
            for (ArrayList subset : rest_subsets) { 
                output.add(new ArrayList(subset)); // Add the subset as is
                ArrayList new_subset = new ArrayList(subset); 
                new_subset.add(0, first); // Add first element to the new subset
                output.add(new_subset); 
            } 

            return output; 
        } else { 
            ArrayList empty_set = new ArrayList<ArrayList>(); 
            empty_set.add(new ArrayList()); 
            return empty_set; 
        } 
    }
}
