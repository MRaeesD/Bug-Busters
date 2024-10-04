package java_programs;
            import java.util.*;


            public class GCD {

                public static int gcd(int a, int b) {
                    if (b == 0) {
                        return a;
                    } else {
                        // Fix: The arguments in the recursive call are swapped
                        return gcd(b, a % b); // The larger number (b) should be the first argument
                    }
                }
            }
