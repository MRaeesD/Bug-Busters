package java_programs;
import java.util.*;

public class SUBSEQUENCES {
    public static ArrayList<ArrayList<Integer>> subsequences(int a, int b, int k) {
        // Corrected return type from ArrayList to ArrayList<ArrayList<Integer>>
        if (k == 0) { 
            return new ArrayList<ArrayList<Integer>>();
        }

        ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>>(50);
        for (int i = a; i < b + 1 - k; i++) {
            ArrayList<ArrayList<Integer>> base = new ArrayList<ArrayList<Integer>>(50);
            for (ArrayList<Integer> rest : subsequences(i + 1, b, k - 1)) {
                rest.add(0, i);
                base.add(rest);
            }
            ret.addAll(base);
        }

        return ret;
    }
}
