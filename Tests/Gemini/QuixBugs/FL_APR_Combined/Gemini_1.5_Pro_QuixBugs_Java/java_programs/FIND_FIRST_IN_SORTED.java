package java_programs;
import java.util.*;


public class FIND_FIRST_IN_SORTED {

    public static int find_first_in_sorted(int[] arr, int x) {
        int lo = 0;
        int hi = arr.length - 1; // FIX 1: Initialize hi to arr.length - 1 to avoid potential ArrayIndexOutOfBoundsException

        while (lo < hi) { // FIX 2: Change <= to < to prevent an infinite loop when x is larger than all elements
            int mid = (lo + hi) / 2; // check if this is floor division

            if (x == arr[mid] && (mid == 0 || x != arr[mid-1])) {
                return mid;
            } else if (x <= arr[mid]) {
                hi = mid - 1; // FIX 3: Update hi to mid - 1 to effectively reduce search space
            } else {
                lo = mid + 1;
            }
        }

        // Check if the last element (when lo == hi) is equal to x
        if (lo < arr.length && arr[lo] == x) { 
            return lo;
        }
        return -1;
    }

}
