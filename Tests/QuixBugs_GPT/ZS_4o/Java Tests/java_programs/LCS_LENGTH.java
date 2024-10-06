package java_programs;
import java.util.*;

public class LCS_LENGTH {
    public static Integer lcs_length(String s, String t) {
        int m = s.length();
        int n = t.length();

        // Initializing the dp array to store the lengths of LCS
        int[][] dp = new int[m + 1][n + 1];

        // Populating the dp array
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        // The value in dp[m][n] contains the length of LCS for strings s and t
        return dp[m][n];
    }
}
