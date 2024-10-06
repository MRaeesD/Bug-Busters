java
package java_programs;
import java.util.*;

public class WRAP {
    public static void main(String[] args) {
        System.out.println("abc".lastIndexOf("c",30));
    }

    public static ArrayList<String> wrap(String text, int cols) {
        ArrayList<String> lines = new ArrayList<String>();

        String line;
        while (text.length() > cols) {
            int end = text.lastIndexOf(" ", cols); // off by one?
            if (end == -1) {
                end = cols;
            }
            line = text.substring(0, end);
            text = text.substring(end).trim();
            lines.add(line);
        }
        
        // Add the remaining text to the list of lines
        lines.add(text);

        return lines;
    }
}
