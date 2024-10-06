package java_programs;
    import java.util.*;

    public class TO_BASE {
        public static String to_base(int num, int b) {
            if (num == 0) return "0"; // Handle edge case for num == 0
            
            String result = "";
            String alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            int i;
            while (num > 0) {
                i = num % b;
                num = num / b;
                result = String.valueOf(alphabet.charAt(i)) + result; // Prepend the digit
            }

            return result;
        }
    }