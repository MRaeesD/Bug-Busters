package java_programs;
import java.util.*;

public class FIND_FIRST_IN_SORTED {

    public static int find_first_in_sorted(int[] arr, int x) {
        int lo = 0;
        int hi = arr.length - 1; // Fix hi to be the last valid index

        while (lo <= hi) {
            int mid = (lo + hi) / 2;

            if (x == arr[mid] && (mid == 0 || x != arr[mid-1])) {
                return mid;
            } else if (x <= arr[mid]) {
                hi = mid - 1; // Change hi to mid - 1
            } else {
                lo = mid + 1;
            }
        }

        return -1;
    }
}