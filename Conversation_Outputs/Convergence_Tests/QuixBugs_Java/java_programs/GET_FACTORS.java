package java_programs;
import java.util.*;

public class GET_FACTORS {
    public static ArrayList<Integer> get_factors(int n) {
        ArrayList<Integer> factors = new ArrayList<Integer>();
        if (n <= 1) { // Edge case for n = 1
            return factors;
        }
        int max = (int)(Math.sqrt(n) + 1.0);
        for (int i = 2; i <= max; i++) { // Adjusted loop condition to include max
            while (n % i == 0) { // Use while to include factor i multiple times
                factors.add(i);
                n /= i;
            }
        }
        if (n > 1) { // If n is a prime number greater than 1
            factors.add(n);
        }
        return factors;
    }
}