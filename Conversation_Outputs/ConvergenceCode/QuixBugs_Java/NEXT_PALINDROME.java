package java_programs;
import java.util.*;

public class NEXT_PALINDROME {
    public static int[] next_palindrome(int[] digit_list) { // Changed return type to int[]
        int n = digit_list.length;
        int high_mid = Math.floorDiv(n, 2);
        int low_mid = Math.floorDiv(n - 1, 2);

        // Check if all digits are 9
        boolean allNines = true;
        for (int digit : digit_list) {
            if (digit != 9) {
                allNines = false;
                break;
            }
        }
        
        if (allNines) {
            int[] result = new int[n + 1];
            result[0] = 1;
            result[n] = 1;
            return result;
        }

        // Increment the palindrome
        while (low_mid >= 0) {
            if (digit_list[low_mid] < 9) {
                digit_list[low_mid]++;
                if (low_mid != high_mid) {
                    digit_list[high_mid]++;
                }
                break;
            } else {
                digit_list[low_mid] = 0;
                digit_list[high_mid] = 0;
            }
            low_mid--;
            high_mid++;
        }

        // Mirror the left side to the right side
        for (int i = 0; i <= low_mid; i++) {
            digit_list[n - 1 - i] = digit_list[i];
        }

        return digit_list; // Return the modified array
    }
}