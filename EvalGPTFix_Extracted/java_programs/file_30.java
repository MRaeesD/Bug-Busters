
import java.io.IOException;
import java.math.BigInteger;
import java.util.*;

public class Main {
    static Scanner in = new Scanner(System.in);


    public static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static void solve() throws IOException {

    }

    public static void main(String arg[]) throws Exception {

        int n = in.nextInt();
        int d = in.nextInt();
        int[] a = new int[n + 1];
        for (int i = 1; i <= n; i++)
            a[i] = in.nextInt();
        for (int i = 2; i <= n; i++)
            if (a[i] - a[i - 1] <= d) {
                System.out.println(a[i - 1]); //bug
                return;
            }
        System.out.println(-1);
    }
}

