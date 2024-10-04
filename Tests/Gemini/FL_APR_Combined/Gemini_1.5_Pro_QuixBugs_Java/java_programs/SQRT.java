package java_programs;
        import java.util.*;
        
        
        public class SQRT { // Class name corrected to follow Java conventions
            public static double sqrt(double x, double epsilon) {
                double approx = x / 2d;
                double prevApprox; 
                // Loop until the absolute difference between successive approximations is less than epsilon
                do {
                    prevApprox = approx; // Store the previous approximation
                    approx = 0.5d * (approx + x / approx); 
                } while (Math.abs(approx - prevApprox) > epsilon); // Check difference between approximations
                return approx;
            }
        }
