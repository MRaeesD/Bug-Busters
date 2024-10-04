package java_programs;
import java.util.*;

public class TO_BASE {
    public static String to_base(int num, int b) {
        StringBuilder result = new StringBuilder(); // Using StringBuilder for efficiency
        String alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        
        while (num > 0) {
            int i = num % b;
            num = num / b; 
            result.insert(0, alphabet.charAt(i)); // Insert at beginning for correct order
        }

        return result.toString();
    }
}