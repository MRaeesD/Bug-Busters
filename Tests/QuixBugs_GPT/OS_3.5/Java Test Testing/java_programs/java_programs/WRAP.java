package java_programs;
import java.util.*;

public class WRAP {
    public static ArrayList<String> wrap(String text, int cols) {
        ArrayList<String> lines = new ArrayList<String>();

        String line;
        while (text.length() > cols) {
            int end = text.lastIndexOf(" ", cols); // off by one?
            if (end == -1) {
                end = cols;
            }
            line = text.substring(0,end);
            text = text.substring(end);
            lines.add(line);
        }
        
        if (!text.isEmpty()) {
            lines.add(text); // add the remaining text as the last line
        }

        return lines;
    }
}