package java_programs;
import java.util.*;


public class SQRT {
    public static double sqrt(double x, double epsilon) {
        double approx = x / 2d;
        double prevApprox = 0; // Initialize previous approximation
        while (Math.abs(approx - prevApprox) > epsilon) { // Compare current and previous approximations
            prevApprox = approx; // Update previous approximation
            approx = 0.5d * (approx + x / approx);
        }
        return approx;
    }
}
