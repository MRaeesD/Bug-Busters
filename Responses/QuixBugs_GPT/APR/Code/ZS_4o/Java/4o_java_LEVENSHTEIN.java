package java_programs;
import java.util.*;

public class LEVENSHTEIN {
    public static int levenshtein(String source, String target) {
        int[][] dp = new int[source.length() + 1][target.length() + 1];

        for (int i = 0; i <= source.length(); i++) {
            for (int j = 0; j <= target.length(); j++) {
                if (i == 0) {
                    dp[i][j] = j; // If source is empty, all insertions
                } else if (j == 0) {
                    dp[i][j] = i; // If target is empty, all deletions
                } else {
                    int cost = source.charAt(i - 1) == target.charAt(j - 1) ? 0 : 1;
                    dp[i][j] = Math.min(Math.min(
                        dp[i - 1][j] + 1,      // Deletion
                        dp[i][j - 1] + 1),     // Insertion
                        dp[i - 1][j - 1] + cost // Substitution
                    );
                }
            }
        }

        return dp[source.length()][target.length()];
    }
}
