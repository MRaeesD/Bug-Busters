package java_programs;
import java.util.*;
import java.util.Arrays;
import java.lang.Math.*;


public class NEXT_PALINDROME {
    public static int[] next_palindrome(int[] digit_list) {
        int high_mid = Math.floorDiv(digit_list.length - 1, 2);
        int low_mid = Math.floorDiv(digit_list.length, 2);
        
        boolean allNines = true;
        for (int digit : digit_list) {
            if (digit != 9) {
                allNines = false;
                break;
            }
        }

        if (allNines) {
            int[] result = new int[digit_list.length + 1];
            result[0] = 1;
            result[result.length - 1] = 1;
            return result;
        }

        while (high_mid >= 0) {
            if (digit_list[high_mid] < 9) {
                digit_list[high_mid]++;
                if (high_mid != low_mid) {
                    digit_list[digit_list.length - high_mid - 1] = digit_list[high_mid];
                }
                break;
            } else {
                digit_list[high_mid] = 0;
                if (high_mid != low_mid) {
                    digit_list[digit_list.length - high_mid - 1] = 0;
                }
            }
            high_mid--;
        }

        for (int i = 0; i < high_mid; i++) {
            digit_list[digit_list.length - i - 1] = digit_list[i];
        }
        
        return digit_list;
    }

    public static void main(String[] args) {
        // Example Usage
        int[] result = next_palindrome(new int[]{1, 4, 9, 4, 1});
        System.out.println(Arrays.toString(result));  // Output: [1, 5, 0, 5, 1]
    }
}