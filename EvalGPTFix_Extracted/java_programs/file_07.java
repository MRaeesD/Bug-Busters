import java.util.ArrayList;
import java.util.Scanner;


public class Main {
    static long mod = 998244353l;
    static long getTenEx(int k) {
        if (k == 0) return 1l;
        if (k == 1) return 10l;
        long tmp = getTenEx(k / 2);
        if (k % 2 == 0) {
            return (tmp * tmp) % mod;
        } else {
            return (tmp * tmp * 10) % mod; //bug
        }
    } 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long num = 1l;
        int f = 0;
        ArrayList<Integer> s = new ArrayList<>();
        s.add(1);
        while (n-- > 0) {
            int ops = sc.nextInt();
            if (ops == 1) {
                
                int x = sc.nextInt();
                num = num * 10 + x;
                num %= mod;
                s.add(x);
            } else if (ops == 2) {
                
                int k = s.size() - f - 1;
                num = (num - s.get(f) * getTenEx(k) + mod * 20) % mod;
                f++;
            } else {
                
                System.out.println(num);
            }
        }
    }
}

