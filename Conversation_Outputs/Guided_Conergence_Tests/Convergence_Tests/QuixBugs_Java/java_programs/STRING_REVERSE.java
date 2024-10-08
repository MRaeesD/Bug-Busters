public class STRING_REVERSE {
    public static String reverse(String str) {
        // Use StringBuilder for efficient string concatenation in the loop
        StringBuilder reversed = new StringBuilder(); 
        for (int i = str.length() - 1; i >= 0; i--) {
            reversed.append(str.charAt(i));
        }
        return reversed.toString();
    }
}