package java_programs;
import java.util.*;

/**
 * This function performs a binary search to find the first occurrence of a given value x in a sorted array.
 * 
 * @param arr A sorted array of integers
 * @param x The value to find
 * @return The lowest index i such that arr[i] == x, or -1 if x is not in arr
 */
public class FIND_FIRST_IN_SORTED {

    public static int find_first_in_sorted(int[] arr, int x) {
        int lo = 0;
        int hi = arr.length - 1; // Initialize hi to the last valid index (arr.length - 1)

        while (lo <= hi) { 
            int mid = (lo + hi) / 2;

            if (x == arr[mid] && (mid == 0 || x != arr[mid-1])) {
                return mid;
            } else if (x <= arr[mid]) {
                hi = mid - 1; 
            } else {
                lo = mid + 1;
            }
        }

        return -1;
    }
}