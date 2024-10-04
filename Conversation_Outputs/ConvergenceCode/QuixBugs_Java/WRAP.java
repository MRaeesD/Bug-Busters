package java_programs;
import java.util.*;

public class WRAP {
    public static void main(String[] args) {
        System.out.println("abc".lastIndexOf("c", 30));
    }

    public static ArrayList<String> wrap(String text, int cols) {
        ArrayList<String> lines = new ArrayList<String>();

        String line;
        while (text.length() > cols) {
            int end = text.lastIndexOf(" ", cols);
            if (end == -1 || end > text.length()) {
                end = cols; // If no space found or end exceeds text length, split at cols
            } else if (text.charAt(end) != ' ') {
                // Move back to the last space if we are in the middle of a word
                while (end > 0 && text.charAt(end) != ' ') {
                    end--;
                }
            }
            line = text.substring(0, end);
            text = text.substring(end).trim(); // Trim leading spaces for the next iteration
            lines.add(line);
        }
        
        // Add any remaining text as the last line
        if (!text.isEmpty()) {
            lines.add(text);
        }

        return lines;
    }
}