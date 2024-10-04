package java_programs;

    public class BITCOUNT {
        public static int bitcount(int n) {
            int count = 0;
            while (n != 0) {
                // Fix: Use bitwise AND (&) with (n - 1) to isolate the rightmost set bit
                n &= (n - 1); 
                count++;
            }
            return count;
        }
    }
