package java_programs;
            import java.util.*;

            public class LCS_LENGTH {
                public static Integer lcs_length(String s, String t) {

                    Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();

                    for (int i = 0; i <= s.length(); i++) {
                        Map<Integer,Integer> initialize = new HashMap<>();
                        for (int j = 0; j <= t.length(); j++) {
                            initialize.put(j, 0);
                        }
                        dp.put(i, initialize);
                    }

                    for (int i = 1; i <= s.length(); i++) {
                        for (int j = 1; j <= t.length(); j++) {
                            if (s.charAt(i - 1) == t.charAt(j - 1)) {
                                dp.get(i).put(j, dp.get(i - 1).get(j - 1) + 1);
                            } else {
                                dp.get(i).put(j, Math.max(dp.get(i - 1).get(j), dp.get(i).get(j - 1)));
                            }
                        }
                    }

                    return dp.get(s.length()).get(t.length());
                }
            }