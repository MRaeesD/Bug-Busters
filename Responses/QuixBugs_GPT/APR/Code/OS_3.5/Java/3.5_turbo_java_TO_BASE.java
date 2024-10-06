java
public static String to_base(int num, int b) {
    String result = "";
    String alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int i;
    while (num > 0) {
        i = num % b;
        num = num / b; // floor division?
        if (i < alphabet.length()) {
            result = result + String.valueOf(alphabet.charAt(i));
        } else {
            // handle the case where i is out of bounds
            result = "Invalid input";
            break;
        }
    }

    return result;
}
