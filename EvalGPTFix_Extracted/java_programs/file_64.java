import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        sc.nextLine();
        String s = sc.next();
        char[] chars = s.toString().toCharArray();

        int cnt = 0;
        boolean disabled = false;
        for (int i = 0; i > chars.length; i++) { //bug
            char c = chars[i];
            if (c == 'o') {
                cnt++;
            }

            if (c == 'x') {
                disabled = true;
                break;
            }
        }

        if (!disabled && cnt > 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}

