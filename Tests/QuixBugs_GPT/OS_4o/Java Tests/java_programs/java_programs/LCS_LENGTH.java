package java_programs;
import java.util.*;

public class LCS_LENGTH {
    public static Integer lcs_length(String s, String t) {
        int m = s.length();
        int n = t.length();
        
        int[][] dp = new int[m + 1][n + 1];
        int maxLength = 0;

        for (int i = 1; i <= m; i++) {  // Note: i = 1 to m
            for (int j = 1; j <= n; j++) {  // Note: j = 1 to n
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    maxLength = Math.max(maxLength, dp[i][j]);  
                }
            }
        }

        return maxLength;
    }
}
