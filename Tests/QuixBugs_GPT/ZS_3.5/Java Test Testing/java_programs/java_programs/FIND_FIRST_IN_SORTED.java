package java_programs;
import java.util.*;


public class FIND_FIRST_IN_SORTED {

    public static int find_first_in_sorted(int[] arr, int x) {
        int lo = 0;
        int hi = arr.length - 1; // Adjusted hi value to prevent out of bounds error
    
        while (lo < hi) { // Updated condition from "lo <= hi" to "lo < hi"
            int mid = lo + (hi - lo) / 2; // check if this is floor division
    
            if (x == arr[mid] && (mid == 0 || x != arr[mid-1])) {
                return mid;
            } else if (x <= arr[mid]) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
    
        return -1;
    }
}