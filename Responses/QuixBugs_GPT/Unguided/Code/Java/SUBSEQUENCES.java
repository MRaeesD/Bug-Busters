package java_programs;
            import java.util.*;
            
            public class SUBSEQUENCES {
                public static ArrayList<ArrayList<Integer>> subsequences(int a, int b, int k) {
                    if (k == 0) {
                        ArrayList<ArrayList<Integer>> emptyList = new ArrayList<>();
                        emptyList.add(new ArrayList<>());
                        return emptyList;
                    }

                    ArrayList<ArrayList<Integer>> ret = new ArrayList<>(50);
                    for (int i = a; i <= b + 1 - k; i++) {
                        for (ArrayList<Integer> rest : subsequences(i + 1, b, k - 1)) {
                            rest.add(0, i);
                            ret.add(rest);
                        }
                    }

                    return ret;
                }
            }