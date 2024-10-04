    package java_programs;
    import java.util.ArrayList;
    
    
    public class SUBSEQUENCES {
        public static ArrayList<ArrayList<Integer>> subsequences(int a, int b, int k) {
            // Fix: If k is 0, return a list containing an empty list to represent an empty subsequence
            if (k == 0) {
                ArrayList<ArrayList<Integer>> emptySubsequence = new ArrayList<>();
                emptySubsequence.add(new ArrayList<>());
                return emptySubsequence;
            }
    
            // Fix: Use default constructor for dynamic sizing
            ArrayList<ArrayList<Integer>> ret = new ArrayList<>(); 
            for (int i = a; i < b + 1 - k; i++) {
                // Fix: Use default constructor for dynamic sizing
                ArrayList<ArrayList<Integer>> base = new ArrayList<>(); 
                for (ArrayList<Integer> rest : subsequences(i + 1, b, k - 1)) {
                    rest.add(0, i);
                    base.add(new ArrayList<>(rest)); // Create a new ArrayList to avoid modifying 'rest'
                }
                ret.addAll(base);
    
            }
    
            return ret;
        }
    }

    