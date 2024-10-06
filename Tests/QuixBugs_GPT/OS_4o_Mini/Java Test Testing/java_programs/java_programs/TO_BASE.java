package java_programs;
import java.util.*;

public class TO_BASE {
    public static String to_base(int num, int b) {
        StringBuilder result = new StringBuilder(); // Changed from String to StringBuilder
        String alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int i;
        while (num > 0) {
            i = num % b;
            num = num / b; // floor division?
            result.append(alphabet.charAt(i)); // Changed to use StringBuilder's append method
        }

        return result.reverse().toString(); // Reverse the result before returning
    }
}
