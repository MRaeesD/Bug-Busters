package java_programs;
import java.util.*;

public class KHEAPSORT {

    public static ArrayList<Integer> kheapsort(ArrayList<Integer> arr, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>();
        for (Integer v : arr.subList(0,k)) {
            heap.add(v);
        }

        ArrayList<Integer> output = new ArrayList<Integer>();
        for (int i = k; i < arr.size(); i++) { // Change starts here
            Integer x = arr.get(i);             // Change continues here
            heap.add(x);
            Integer popped = heap.poll();
            output.add(popped);
        } // Change ends here

        while (!heap.isEmpty()) {
            output.add(heap.poll());
        }

        return output;
    }
}
