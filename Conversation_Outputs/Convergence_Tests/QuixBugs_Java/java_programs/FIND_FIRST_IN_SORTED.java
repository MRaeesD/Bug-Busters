package java_programs;
import java.util.*;
import java_programs.Node;

public class FIND_FIRST_IN_SORTED {

    public static int find_first_in_sorted(int[] arr, int x) {
        int lo = 0;
        int hi = arr.length - 1; // Fixed: Initialize hi to arr.length - 1

        while (lo <= hi) { // Corrected loop condition
            int mid = (lo + hi) / 2;

            if (x == arr[mid] && (mid == 0 || arr[mid-1] != x)) { // Simplified condition
                return mid;
            } else if (x <= arr[mid]) {
                hi = mid - 1; // Adjusted to ensure we don't skip potential targets
            } else {
                lo = mid + 1;
            }
        }

        return -1;
    }
}