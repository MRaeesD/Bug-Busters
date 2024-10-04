package java_programs;
import java.util.*;


public class LCS_LENGTH {
    public static Integer lcs_length(String s, String t) {
        int[][] dp = new int[s.length() + 1][t.length() + 1]; // Use a 2D array for DP table
        int maxLength = 0; // Variable to track the maximum length of common substring

        for (int i = 1; i <= s.length(); i++) { // Start from 1 to avoid off-by-one errors
            for (int j = 1; j <= t.length(); j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1; // Correct DP transition using diagonal
                    maxLength = Math.max(maxLength, dp[i][j]); // Update maxLength
                } else {
                    dp[i][j] = 0; // Reset for non-matching characters
                }
            }
        }

        return maxLength; // Return the length of the longest common substring
    }
}