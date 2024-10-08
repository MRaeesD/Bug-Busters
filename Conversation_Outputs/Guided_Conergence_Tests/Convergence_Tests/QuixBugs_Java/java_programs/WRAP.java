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
            int end = text.lastIndexOf(" ", cols);
            if (end == -1) {
                end = cols;
            }
            line = text.substring(0,end);
            text = text.substring(end);
            lines.add(line);
        }

        // Add any remaining text that is less than or equal to cols
        if (text.length() > 0) { 
            lines.add(text);
        }

        return lines;
    }
}