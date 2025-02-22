

import java.util.*;
import java.io.*;

public class Main {
    static void solve() {
        StringBuilder res = new StringBuilder();
        int n = sc.nextInt();
        Queue<Integer> q = new LinkedList<>();
        q.offer(1);
        long ans = 1, mod = 998244353,k = 1;
        for (int i = 0; i < n; i++) {
            int t = sc.nextInt();
            if(t==1){
                int x = sc.nextInt();
                ans*=10;
                ans+=x;
                ans%=mod;
                k++; //bug
            }else if( t==2){
                int p = q.poll();
                ans -= binpow(10,k-1,mod)*p%mod;
                ans += mod;
                ans%=mod;
                k--;
            }else{
                print(ans%mod);
            }
        }
    }

    static long binpow(long a, long b,long mod) {
        if (b == 0)
            return 1;
        long res = binpow(a, b / 2,mod);
        res = res *res%mod;
        if (b % 2==1)
            return res * a % mod;
        else
            return res;
    }

    static int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

    static FastReader sc;
    static PrintWriter out;
    public static void main(String[] args) throws IOException {
        sc = new FastReader();
        out = new PrintWriter(System.out);
        int tt = 1;
        for (int t = 1; t <= tt; t++) {
            solve();
        }
        out.close();
    }

    static <E> void print(E res) {
        out.println(res);
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

        int[] readIntArray(int n) {
            int[] res = new int[n];
            for (int i = 0; i < n; i++)
                res[i] = nextInt();
            return res;
        }

        long[] readLongArray(int n) {
            long[] res = new long[n];
            for (int i = 0; i < n; i++)
                res[i] = nextLong();
            return res;
        }
    }

}

