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

        for (Integer x : arr.subList(1, arr.size())) {
            if (x < pivot) {
                lesser.add(x);
            } else if (x >= pivot) { // Change made here
                greater.add(x);
            }
        }
        ArrayList<Integer> middle = new ArrayList<Integer>();
        middle.add(pivot);
        lesser = quicksort(lesser);
        greater = quicksort(greater);
        middle.addAll(greater);
        lesser.addAll(middle);
        return lesser;

    }
}
