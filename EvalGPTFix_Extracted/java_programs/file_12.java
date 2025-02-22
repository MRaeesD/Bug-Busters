import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;

public class Main {

    
    long modPow(long x, long n, long mod) {
        long ret = 1;
        while (n > 0) {
            if ((n & 1) == 1) ret = ret * x % mod;
            x = x * x % mod;
            n >>= 1;
        }
        return ret;
    }

    void solve() {
        int Q = nextInt();
        Deque<Integer> S = new ArrayDeque<>();
        S.push(1);
        long mod = 998244353;
        long remainder = 1;
        for (int q = 0; q < Q; q++) {
            int type = nextInt();
            if (type == 1) {
                int x = nextInt();
                S.addLast(x);
                remainder = (10 * remainder + x) % mod;
            } else if (type == 2) {
                int x = S.pollFirst();
                remainder = (remainder - x * modPow(10, S.size(), mod)) % mod; //bug
            } else {
                println(remainder);
            }
        }
    }

    
    public static void main(String[] args) {
        Main main = new Main();
        main.solve();
        flush();
    }

    
    static FastReader fr = new FastReader();

    static String next() {
        return fr.next();
    }

    static int nextInt() {
        return fr.nextInt();
    }

    static class FastReader {

        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    
    static PrintWriter out = new PrintWriter(System.out);

    static void println(Object o) {
        out.println(o);
    }

    static void flush() {
        out.flush();
    }
}

