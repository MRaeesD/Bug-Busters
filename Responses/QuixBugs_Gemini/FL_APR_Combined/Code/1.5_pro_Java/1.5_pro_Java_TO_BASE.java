package java_programs;
    import java.util.*;


    public class TO_BASE {
        public static String to_base(int num, int b) {
            String result = "";
            String alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            int i;
            while (num > 0) {
                i = num % b;
                num = num / b; 
                // The bug was here. The string concatenation was adding the newest digit to the beginning of the result
                // result = result + String.valueOf(alphabet.charAt(i));
                // The fix is to add the newest digit to the end of the result
                result = String.valueOf(alphabet.charAt(i)) + result;
            }

            return result;
        }
    }
