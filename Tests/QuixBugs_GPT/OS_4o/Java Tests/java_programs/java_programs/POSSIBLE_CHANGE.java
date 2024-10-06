package java_programs; // missing the package declaration
import java.util.*;

public class POSSIBLE_CHANGE {
    public static int possible_change(int[] coins, int total) {
        // Memoization array to store results of previously computed values
        int[] dp = new int[total + 1];
        dp[0] = 1; // Base case: There's one way to make 0 total, by using no coins

        // For each coin, we update the dp array
        for (int coin : coins) {
            for (int j = coin; j <= total; j++) {
                dp[j] += dp[j - coin];
            }
        }

        return dp[total];
    }
}
