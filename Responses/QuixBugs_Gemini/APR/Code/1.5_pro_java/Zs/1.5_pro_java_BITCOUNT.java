package java_programs;

public class BITCOUNT {
    public static int bitcount(int n) {
        int count = 0;
        while (n != 0) {
            n &= (n - 1); // Use bitwise AND with n-1 to clear the rightmost set bit
            count++;
        }
        return count;
    }
}
