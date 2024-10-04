package java_programs;
import java.util.*;

public class KHEAPSORT {

    public static ArrayList<Integer> kheapsort(ArrayList<Integer> arr, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>();
        
        // Initialize the heap with the first k elements
        for (Integer v : arr.subList(0, k)) {
            heap.add(v);
        }

        ArrayList<Integer> output = new ArrayList<Integer>();

        // Start the loop from the kth element, as the first k elements are already in the heap
        for (int i = k; i < arr.size(); i++) {
            heap.add(arr.get(i)); // Add the current element to the heap
            Integer popped = heap.poll(); // Poll the smallest element
            output.add(popped); // Add it to the output list
        }

        // Poll remaining elements from the heap
        while (!heap.isEmpty()) {
            output.add(heap.poll());
        }

        return output;
    }
}