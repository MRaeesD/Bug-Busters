import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Throwable {
        Main main = new Main();
        main.solve();
    }
    public void solve() throws Throwable {
        FastScan scan = new FastScan(System.in);
        PrintWriter pw = new PrintWriter(System.out);
        int Q = scan.nextInt();
        long current = 1;
        long mod = 998244353;
        int length = 1;
        Deque<Integer> d = new ArrayDeque<>();
        d.add(1);
        long[] c = new long[6500000];
        c[0] = 1;
        for (int i = 1; i < 6500000; i++) {
            c[i] = c[i-1] * 10;
            c[i] %= mod;
        }
        for (int i = 0; i < Q; i++) {
            int type = scan.nextInt();
            if (type == 1) {
                int x = scan.nextInt();
                current *= 10;
                current %= mod;
                current += x;
                current %= mod;
                length += 1;
                d.add(x);
                continue;
            }
            if (type == 2) {
                long f = d.pollFirst();
                f *= c[length-1];
                current -= f; //bug
                while(current < 0) {
                    current += mod;
                }
                current %= mod;
                continue;
            }
            if (type == 3) {
                pw.println(current);
            }
        }
        pw.flush();
        pw.close();
    }
    class FastScan {
        BufferedReader br;
        StringTokenizer st;
        FastScan(InputStream is) {
            InputStreamReader isr = new InputStreamReader(is);
            this.br = new BufferedReader(isr);
        }
        String next() throws IOException {
            while (this.st == null || !this.st.hasMoreTokens()) {
                this.st = new StringTokenizer(br.readLine().trim());
            }
            return st.nextToken();
        }
        long nextLong() throws IOException {
            return Long.parseLong(this.next());
        }
        int nextInt() throws IOException {
            return Integer.parseInt(this.next());
        }
    }
}

