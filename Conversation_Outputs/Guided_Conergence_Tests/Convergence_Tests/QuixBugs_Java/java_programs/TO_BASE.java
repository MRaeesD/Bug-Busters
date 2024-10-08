package java_programs;
import java.util.*;

public class TO_BASE {
    public static String to_base(int num, int b) {
        StringBuilder result = new StringBuilder();
        String alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int i;
        while (num > 0) {
            i = num % b;
            num = num / b; // floor division
            result.insert(0, alphabet.charAt(i)); // Prepend the character
        }

        return result.toString();
    }
}