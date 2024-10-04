package java_programs;
    import java.util.*;
    
    
    public class WRAP {
        public static void main(String[] args) {
            // Test cases
            String text = "This is a long string that needs to be wrapped.";
            int cols = 15;
            ArrayList<String> wrappedText = wrap(text, cols);
            for (String line : wrappedText) {
                System.out.println(line);
            }
        }
    
        public static ArrayList<String> wrap(String text, int cols) {
            ArrayList<String> lines = new ArrayList<String>();
    
            String line;
            while (text.length() > cols) {
                int end = text.lastIndexOf(" ", cols); // Find the last space before the column limit
                if (end == -1) { 
                    end = cols; 
                } else {
                    end++; // Move end index past the space to exclude it from the current line
                }
                line = text.substring(0, end);
                // If a space was found, move the start index past the space to avoid extra spaces
                if (end < text.length() && text.charAt(end) == ' ') { 
                    text = text.substring(end + 1); 
                } else {
                    text = text.substring(end);
                }
                lines.add(line);
            }
            if(text.length()>0){
                lines.add(text);
            }
    
            return lines;
        }
    }
