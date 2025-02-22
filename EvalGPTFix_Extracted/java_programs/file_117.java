import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        long A = scanner.nextLong();
        long B = scanner.nextLong();

        if (B > A) {
            long temp = B;
            B = A;
            A = temp;
        }

        if (A == B) {
            System.out.println(0);
            return;
        }

        long p = A;
        long q = B;
        long res = 0;

        while (p % q != 0) { //bug
            res += p / q;

            long temp = q;
            q = p % q;
            p = temp;
        }

        System.out.println(res + 1);
    }
}

