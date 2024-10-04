package java_programs;
            import java.util.*;

            public class KHEAPSORT {

                public static ArrayList<Integer> kheapsort(ArrayList<Integer> arr, int k) {
                    PriorityQueue<Integer> heap = new PriorityQueue<Integer>();
                    for (Integer v : arr.subList(0,k)) {
                        heap.add(v);
                    }

                    ArrayList<Integer> output = new ArrayList<Integer>();
                    // Bug fix: Start iterating from the (k+1)th element
                    for (int i = k; i < arr.size(); i++) { 
                        // Bug fix: Remove the erroneous addition of elements
                        Integer popped = heap.poll(); 
                        output.add(popped);
                        heap.add(arr.get(i));
                    }

                    while (!heap.isEmpty()) {
                        output.add(heap.poll());
                    }

                    return output;

                }
            }
