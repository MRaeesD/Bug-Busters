package java_programs;
import java.util.*;


public class SUBSEQUENCES {
    public static ArrayList<ArrayList<Integer>> subsequences(int a, int b, int k) {
        if (k == 0) {
            ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
            result.add(new ArrayList<Integer>()); // Add an empty list to represent a subsequence of length 0
            return result;
        }

        ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>>(50);
        for (int i=a; i<b+1-k; i++) {
            ArrayList<ArrayList<Integer>> base = new ArrayList<ArrayList<Integer>>(50);
            for (ArrayList<Integer> rest : subsequences(i+1, b, k-1)) {
                rest.add(0,i);
                base.add(rest);
            }
            ret.addAll(base);

        }

        return ret;
    }
}