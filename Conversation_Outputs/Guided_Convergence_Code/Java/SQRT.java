package java_programs;
import java.util.*;

public class SQRT {
    public static double sqrt(double x, double epsilon) {
        // Check preconditions
        if (x < 1 || epsilon <= 0) {
            throw new IllegalArgumentException("x should be >= 1 and epsilon should be > 0");
        }
        
        double approx = x / 2d;
        /* Bug: Incorrect condition in the while loop for checking convergence.
           Fix: The condition should compare the difference between the square of the approximation
                 and the original number to epsilon. */
        while (Math.abs(approx * approx - x) > epsilon) { 
            approx = 0.5d * (approx + x / approx);
        }
        return approx;
    }
}