package java_programs;
import java.util.*;

public class POSSIBLE_CHANGE {
    public static int possible_change(int[] coins, int total) {
        // Base case: If total is 0, we've found a valid combination
        if (total == 0) {
            return 1;
        }
        // If total is negative or no coins are left, no valid combination
        if (total < 0 || coins.length == 0) { // Fix: Added check for empty coins array to prevent ArrayIndexOutOfBoundsException
            return 0;
        }

        // Using the first coin
        int useFirst = possible_change(coins, total - coins[0]);

        // Not using the first coin, move to the next coin
        int[] rest = Arrays.copyOfRange(coins, 1, coins.length);
        int skipFirst = possible_change(rest, total);

        return useFirst + skipFirst;
    }
}