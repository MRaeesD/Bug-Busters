import java.util.*;


public class WRAP {
    public static void main(String[] args) {
        System.out.println("abc".lastIndexOf("c",30));
    }

    public static ArrayList<String> wrap(String text, int cols) {
        ArrayList<String> lines = new ArrayList<String>();

        String line;
        while (text.length() > cols) { // Original code had no closing curly brace
            int end = text.lastIndexOf(" ", cols); // off by one?
            if (end == -1) {
                end = cols;
            }
            line = text.substring(0,end);
            text = text.substring(end);
            lines.add(line);
        }
        if (text.length() > 0) {  // Added to append rest of text
            lines.add(text);
        }

        return lines;
    }
}
