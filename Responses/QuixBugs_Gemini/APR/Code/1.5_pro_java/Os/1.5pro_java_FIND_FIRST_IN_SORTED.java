Fix:

package java_programs;
import java.util.*;


public class FIND_FIRST_IN_SORTED {

    public static int find_first_in_sorted(int[] arr, int x) {
        int lo = 0;
        int hi = arr.length;

        while (lo < hi) { // Changed <= to < to avoid 'lo' reaching 'hi'
            int mid = (lo + hi) / 2; 

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
