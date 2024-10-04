package java_programs;
import java.util.*;

public class POWERSET {
    public static ArrayList<ArrayList> powerset(ArrayList arr) {
        if (!arr.isEmpty()) {
            Object first = arr.get(0);
            
            // Avoid modifying the input list directly to prevent side effects.
            ArrayList rest = new ArrayList(arr.subList(1, arr.size())); 
            ArrayList<ArrayList> rest_subsets = powerset(rest);

            ArrayList<ArrayList> output = new ArrayList<ArrayList>();
            output.addAll(rest_subsets); 

            // Create new 'to_add' list inside the loop to generate distinct subsets.
            for (ArrayList subset : rest_subsets) {
                ArrayList to_add = new ArrayList();
                to_add.add(first);
                to_add.addAll(subset);
                output.add(to_add);
            }

            return output;
        } else {
            ArrayList empty_set = new ArrayList<ArrayList>();
            empty_set.add(new ArrayList());
            return empty_set;
        }
    }
}