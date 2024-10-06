package java_programs;
import java.util.*;

public class SUBSEQUENCES {
    public static ArrayList<ArrayList<Integer>> subsequences(int a, int b, int k) { // Corrected the return type
        if (k == 0) {
            return new ArrayList<>(); // Corrected the return type
        }

        ArrayList<ArrayList<Integer>> ret = new ArrayList<>(50); // Corrected the list type
        for (int i = a; i < b + 1 - k; i++) {
            ArrayList<ArrayList<Integer>> base = new ArrayList<>(50); // Corrected the list type
            for (ArrayList<Integer> rest : subsequences(i + 1, b, k - 1)) { // Corrected the list type
                rest.add(0, i);
                base.add(rest);
            }
            ret.addAll(base);
        }

        return ret;
    }
}
