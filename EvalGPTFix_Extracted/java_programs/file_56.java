以下は、問題を解くJavaのコード例です。 //bug

java
Copy code
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        String s = scanner.next();

        boolean goodExist = false;
        boolean badExist = false;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'o') {
                goodExist = true;
            } else if (s.charAt(i) == 'x') {
                badExist = true;
            }
        }

        if (goodExist && !badExist) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}

