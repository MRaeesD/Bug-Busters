import java.nio.charset.StandardCharsets;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class Main {
    private static final int MOD = 998244353;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in, StandardCharsets.UTF_8);
        int q = scanner.nextInt();

        long res = 1L;
        Deque<Integer> deque = new ArrayDeque<>();
        deque.addLast(1);
        while (q-- > 0) {
            int op = scanner.nextInt();
            if (op == 1) {
                int x = scanner.nextInt();
                deque.addLast(x);
                res = (res * 10 + x) % MOD;
            } else if (op == 2) {
                int y = deque.removeFirst();
                int sz = deque.size();
                res = (res - y * quickPow(10, sz) + MOD) % MOD; //bug
            } else {
                System.out.println(res);
            }
        }
    }

    
    private static long quickPow(long a, long b) {
        long res = 1L;
        while (b > 0) {
            if ((b & 1) == 1) {
                res = res * a % MOD;
            }
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }
}

