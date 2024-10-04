package java_programs;
import java.util.*;

public class SIEVE {

    public static ArrayList<Integer> sieve(Integer max) {
        // Boolean array to mark non-prime numbers
        boolean[] is_prime = new boolean[max + 1];
        Arrays.fill(is_prime, true);
        
        // Start from the first prime number, 2
        for (int p = 2; p * p <= max; p++) {
            // If p is a prime, mark its multiples as non-prime
            if (is_prime[p]) {
                for (int multiple = p * p; multiple <= max; multiple += p) {
                    is_prime[multiple] = false;
                }
            }
        }
        
        // Collect all prime numbers
        ArrayList<Integer> primes = new ArrayList<>();
        for (int n = 2; n <= max; n++) {
            if (is_prime[n]) {
                primes.add(n);
            }
        }
        
        return primes;
    }
}