package java_programs;
import java.util.*;

public class SQRT {
    public static double sqrt(double x, double epsilon) {
        // Handle division by zero case
        if (x == 0) return 0; // Return 0 immediately for x == 0

        double approx = x / 2d;
        // Corrected while loop condition
        while (Math.abs(approx * approx - x) > epsilon) { // Check the difference between square of approx and x
            approx = 0.5d * (approx + x / approx);
        }
        return approx;
    }
}