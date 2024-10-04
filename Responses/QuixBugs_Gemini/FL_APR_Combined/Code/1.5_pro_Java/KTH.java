package java_programs;
            import java.util.*;
            public class KTH {
                public static Integer kth(ArrayList<Integer> arr, int k) {
                    int pivot = arr.get(0);
                    ArrayList<Integer> below = new ArrayList<>(); // Fix: Removed unnecessary initial capacity
                    ArrayList<Integer> above = new ArrayList<>(); // Fix: Removed unnecessary initial capacity
                    for (Integer x : arr) {
                        if (x < pivot) {
                            below.add(x);
                        } else if (x > pivot) {
                            above.add(x);
                        }
                    }

                    int num_less = below.size();
                    int num_lessoreq = arr.size() - above.size();
                    if (k < num_less) {
                        return kth(below, k);
                    } else if (k >= num_lessoreq) {
                        return kth(above, k - num_lessoreq); // Fix: Adjusted k for the 'above' subproblem
                    } else {
                        return pivot;
                    }
                }
            }
