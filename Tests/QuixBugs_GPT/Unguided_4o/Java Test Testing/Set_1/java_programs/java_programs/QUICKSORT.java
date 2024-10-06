package java_programs;
import java.util.*;

public class QUICKSORT {
    public static ArrayList<Integer> quicksort(ArrayList<Integer> arr) {
        if (arr.isEmpty()) {
            return new ArrayList<Integer>();
        }

        Integer pivot = arr.get(0);
        ArrayList<Integer> lesser = new ArrayList<Integer>();
        ArrayList<Integer> greater = new ArrayList<Integer>();
        ArrayList<Integer> equal = new ArrayList<Integer>();

        for (Integer x : arr) {
            if (x < pivot) {
                lesser.add(x);
            } else if (x > pivot) {
                greater.add(x);
            } else {
                equal.add(x);
            }
        }

        lesser = quicksort(lesser);
        greater = quicksort(greater);
        lesser.addAll(equal);
        lesser.addAll(greater);

        return lesser;
    }
}