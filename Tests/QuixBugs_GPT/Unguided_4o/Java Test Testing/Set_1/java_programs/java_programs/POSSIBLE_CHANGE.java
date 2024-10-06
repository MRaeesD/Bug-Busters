package java_programs;
import java.util.*;

public class POSSIBLE_CHANGE {
    public static int possible_change(int[] coins, int total) {
        return possible_change_helper(coins, total, 0);
    }
    
    private static int possible_change_helper(int[] coins, int total, int index) {
        if (total == 0) {
            return 1;
        }
        if (total < 0 || index == coins.length) {
            return 0;
        }

        int countWithCoin = possible_change_helper(coins, total - coins[index], index);
        int countWithoutCoin = possible_change_helper(coins, total, index + 1);

        return countWithCoin + countWithoutCoin;
    }
}