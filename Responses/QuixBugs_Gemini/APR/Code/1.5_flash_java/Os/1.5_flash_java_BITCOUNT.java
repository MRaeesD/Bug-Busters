package java_programs;

public class BITCOUNT {
    public static int bitcount(int n) {
    int count = 0;
    while (n != 0) {
        // Correct the code to use the AND operation with 1 to check the least significant bit
        n &= (n - 1);
        count++;
    }
    return count;
    }
}
