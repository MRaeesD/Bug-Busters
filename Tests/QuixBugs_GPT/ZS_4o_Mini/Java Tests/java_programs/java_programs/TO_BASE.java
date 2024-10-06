package java_programs;
import java.util.*;

public class TO_BASE {
    public static String to_base(int num, int b) {
        StringBuilder result = new StringBuilder(); // Changed to StringBuilder for efficiency
        String alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int i;
        while (num > 0) {
            i = num % b;
            num = num / b;
            result.append(alphabet.charAt(i)); // Changed to append method of StringBuilder
        }
        
        return result.reverse().toString(); // Reverse the result before returning
    }
}
