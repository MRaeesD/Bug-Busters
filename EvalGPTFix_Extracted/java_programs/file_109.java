import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long A = sc.nextInt(); //bug
        long B = sc.nextInt();

        if (A > B) {
            long tmp = B;
            B = A;
            A = tmp;
        }

        long ans = solve(A, B);
        System.out.println(ans);
    }

    private static long solve(long A, long B) {
        if(A == B) {
            return 0;
        }
        long cnt = B / A;
        long mod = B % A;
        if(mod == 0) {
            return cnt - 1;
        }
        return solve(mod, A) + cnt;
    }
}

