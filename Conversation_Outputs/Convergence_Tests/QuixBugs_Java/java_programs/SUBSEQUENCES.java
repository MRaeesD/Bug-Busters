package java_programs;
import java.util.*;

public class SUBSEQUENCES {
    public static ArrayList<ArrayList<Integer>> subsequences(int a, int b, int k) {
        if (k == 0) {
            ArrayList<ArrayList<Integer>> baseCase = new ArrayList<>();
            baseCase.add(new ArrayList<>()); // Fix: Return a list containing an empty list
            return baseCase;
        }

        ArrayList<ArrayList<Integer>> ret = new ArrayList<>(); // Fix: Use generic type and no fixed capacity
        for (int i = a; i <= b - k + 1; i++) { // Fix: Adjust loop condition
            for (ArrayList<Integer> rest : subsequences(i + 1, b, k - 1)) {
                ArrayList<Integer> newList = new ArrayList<>(rest); // Fix: Create a new list
                newList.add(0, i);
                ret.add(newList);
            }
        }

        return ret;
    }
}