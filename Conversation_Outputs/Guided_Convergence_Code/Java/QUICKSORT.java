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
        ArrayList<Integer> middle = new ArrayList<Integer>(); // Declare middle here

        for (Integer x : arr.subList(1, arr.size())) {
            if (x < pivot) {
                lesser.add(x);
            } else if (x == pivot) { // Directly add elements equal to pivot to 'middle'
                middle.add(x);
            } else { 
                greater.add(x);
            }
        }
        
        middle.add(pivot); // Add pivot to middle
        lesser = quicksort(lesser);
        greater = quicksort(greater);
        middle.addAll(greater);
        lesser.addAll(middle);
        return lesser;
    }
}