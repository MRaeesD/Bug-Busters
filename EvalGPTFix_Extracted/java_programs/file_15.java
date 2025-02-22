import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader()
        {
            br = new BufferedReader(
                    new InputStreamReader(System.in));
        }

        String next()
        {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }

        long nextLong() { return Long.parseLong(next()); }

        double nextDouble()
        {
            return Double.parseDouble(next());
        }

        String nextLine()
        {
            String str = "";
            try {
                if(st.hasMoreTokens()){
                    str = st.nextToken("\n");
                }
                else{
                    str = br.readLine();
                }
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }

    static long modPow(long x, long n, long mod) {
        long result = 1;
        while (n > 0) {
            if ((n & 1) == 1) {
                result = result * x % mod;
            }
            x = x * x % mod;
            n >>= 1;
        }
        return result;
    }

    public static void main(String[] args) {
        FastReader scanner = new FastReader();
        long number = 1;
        long mod = 998244353;
        int q = scanner.nextInt();

        Deque<Integer> deque = new ArrayDeque<>();
        deque.offerLast(1);

        for (int i = 0; i < q; i++) {
            int option = scanner.nextInt();
            switch (option) {
                case 1:
                    int x = scanner.nextInt();
                    deque.offerLast(x);
                    number = (number * 10 + x) % mod;
                    break;
                case 2:
                    int upper = deque.pollFirst();
                    number = (number - upper * modPow(10, deque.size(), mod)) % mod; //bug
                    break;
                case 3:
                    System.out.println(number);
                    break;
            }
        }
    }
}

