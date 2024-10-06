java
package java_programs;
import java.util.*;

public class LCS_LENGTH {
    public static Integer lcs_length(String s, String t) {

        Map<Integer, Map<Integer,Integer>> dp = new HashMap<Integer,Map<Integer,Integer>>();

        for (int i=0; i <= s.length(); i++) {  // Changed to i <= s.length()
            Map<Integer,Integer> initialize = new HashMap<Integer,Integer>();
            dp.put(i, initialize);
            for (int j=0; j <= t.length(); j++) {  // Changed to j <= t.length()
                Map<Integer,Integer> internal_map = dp.get(i);
                internal_map.put(j,0);
                dp.put(i, internal_map);
            }
        }

        for (int i=1; i <= s.length(); i++) {  // Start from 1
            for (int j=1; j <= t.length(); j++) {  // Start from 1
                if (s.charAt(i-1) == t.charAt(j-1)) {  // Adjusted indexing

                    Map<Integer, Integer> internal_map = dp.get(i);
                    int insert_value = dp.get(i-1).get(j-1) + 1;  // Use j-1
                    internal_map.put(j, insert_value);
                    dp.put(i,internal_map);
                } else {
                    // Update for not matching
                    Map<Integer, Integer> internal_map = dp.get(i);
                    int maxVal = Math.max(dp.get(i - 1).get(j), dp.get(i).get(j - 1));
                    internal_map.put(j, maxVal);
                    dp.put(i,internal_map);
                }
            }
        }

        if (!dp.isEmpty()) {
            List<Integer> ret_list = new ArrayList<Integer>();
            for (int i=0; i<=s.length(); i++) {  // Expand to include last row
                ret_list.add(!dp.get(i).isEmpty() ? Collections.max(dp.get(i).values()) : 0);
            }
            return Collections.max(ret_list);
        } else {
            return 0;
        }
    }
}
