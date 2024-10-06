java
package java_programs;
import java.util.*;

public class KHEAPSORT {

    public static ArrayList<Integer> kheapsort(ArrayList<Integer> arr, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>();
        for (Integer v : arr.subList(0,k)) {
            heap.add(v);
        }

        ArrayList<Integer> output = new ArrayList<Integer>();
        for (int i = k; i < arr.size(); i++) { // Changed the loop to start from k
            heap.add(arr.get(i));
            output.add(heap.poll());
        }

        while (!heap.isEmpty()) {
            output.add(heap.poll());
        }

        return output;

    }
}
