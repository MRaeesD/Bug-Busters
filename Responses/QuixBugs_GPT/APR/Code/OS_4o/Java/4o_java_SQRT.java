package java_programs;
import java.util.*;

public class SQRT {
    public static double sqrt(double x, double epsilon) {
        double approx = x / 2d;
        // Correct the loop condition as stated above
        while (Math.abs(approx * approx - x) > epsilon) {  // Fixed loop condition
            approx = 0.5d * (approx + x / approx);
        }
        return approx;
    }
}
