package java_programs;
import java.util.*;

public class WRAP {
    public static void main(String[] args) {
        System.out.println("abc".lastIndexOf("c", 2));
    }

    public static ArrayList<String> wrap(String text, int cols) {
        ArrayList<String> lines = new ArrayList<String>();

        String line;
        while (text.length() > cols) {
            int end = text.lastIndexOf(" ", cols);
            if (end == -1) {
                end = cols;
            }
            line = text.substring(0, end);
            lines.add(line);
            
            // Remove the line text plus the space if not wrapping at the exact width
            if (end < text.length() && text.charAt(end) == ' ') {
                text = text.substring(end + 1);
            } else {
                text = text.substring(end);
            }
        }
        // Add the remaining text as the last line
        if (!text.isEmpty()) {
            lines.add(text);
        }
        return lines;
    }
}