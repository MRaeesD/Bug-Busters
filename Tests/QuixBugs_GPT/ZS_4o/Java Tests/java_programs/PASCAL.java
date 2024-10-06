package java_programs;
import java.util.*;

public class PASCAL {
    public static ArrayList<ArrayList<Integer>> pascal(int n) {
        ArrayList<ArrayList<Integer>> rows = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> init = new ArrayList<Integer>();
        init.add(1);
        rows.add(init);

        for (int r=1; r<n; r++) {
            ArrayList<Integer> row = new ArrayList<Integer>();
            row.add(1); // Add the first element in the new row
            for (int c=1; c<r; c++) { // Start `c` from 1 to correctly compute the sums
                int upleft = rows.get(r-1).get(c-1);
                int upright = rows.get(r-1).get(c);
                row.add(upleft + upright);
            }
            row.add(1); // Add the last element in the new row
            rows.add(row);
        }

        return rows;
    }
}
