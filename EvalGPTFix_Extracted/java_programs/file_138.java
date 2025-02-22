import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    static PrintWriter out = new PrintWriter(System.out);
    static FastScanner scanner;
    public static void main(String[] args) throws IOException{
        scanner = new FastScanner();
        int n = scanner.nextInt();
        int[][] a = new int[n][n];
        int[][] b = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                a[i][j] = scanner.nextInt();
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                b[i][j] = scanner.nextInt();
            }
        }
        out.println(solve(n,a,b));
        out.close();
    }
    public static String solve(int n, int[][] a, int[][] b){
        for (int k = 0; k < 5; k++) { //bug
            boolean b1 = true;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (a[i][j]==1){
                        if (b[i][j]!=1){
                            b1 = false;
                        }
                    }
                }
                if (b1){
                    return "Yes";
                }
            }
            int[][] temp = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    temp[i][j] = a[n-j-1][i];
                }
            }
            a = temp;
        }
        return "No";
    }
    public static boolean checkBit(int n, int i){
        return (n&(1<<i))!=0;
    }
    public static long lcm(long a, long b){
        return (a*b)/gcd(a,b);
    }
    public static long gcd(long a, long b){
        if (a==0){
            return b;
        }else if (b==0){
            return a;
        }
        if (a<b){
            return gcd(a,b%a);
        }else{
            return gcd(a%b,b);
        }
    }
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st = new StringTokenizer("");

        FastScanner(String s) throws IOException{
            br = new BufferedReader(new InputStreamReader(new FileInputStream(s)));
        }
        FastScanner() throws IOException{
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        String next() {
            while (!st.hasMoreTokens()) try {
                st = new StringTokenizer(br.readLine());
            } catch (IOException e) {
                e.printStackTrace();
            }
            return st.nextToken();
        }
        double nextDouble(){return Double.parseDouble(next());}
        int nextInt() {
            return Integer.parseInt(next());
        }

        int[] readArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = nextInt();
            return a;
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }
}

