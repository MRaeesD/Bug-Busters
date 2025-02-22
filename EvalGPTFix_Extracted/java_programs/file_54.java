
import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
	
	 	public static int psi(String n) {
	 		return Integer.parseInt(n);
	 	}

	    public static long psl(String n) {
	        return Long.parseLong(n);
	    }

	    public static String str_int(int n) {
	       return String.valueOf(n);
	    }

	   public static String str_lg(long n) {
	       return String.valueOf(n);
	   }
	   
	   
	   public static void dfs (List<List<Integer>> arr, boolean [] memo, int v) {
		   	memo[v] = true;
		   	
		   	for (int u : arr.get(v)) {
		   		if (memo[u]) continue;
		   		dfs(arr, memo, u);
		   	}
	   }
	   
	   
	   public static int bin_pw(int a, int p, int mod) {
		   	int ans = 1;
		   	
		   	while (p > 0) {
		   		if (p % 2 == 1) ans = (int) (((long) ans * a) % mod);
		   		
		   		p /= 2;
		   		a = (int) (((long) a * a) % mod);
		   	}
		   	
		   	return ans;
	   }
	   
	   
	   public static int div_mod(int a, int b, int mod) {
		   return (int) (((long) (a % mod) * bin_pw(b % mod, mod - 2, mod)) % mod);
	   }
	   
	   
	public static void main(String[] args) throws java.lang.Exception {
		BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);


        

        	
        	int mod = 998244353;
        	
        	String [] vals = rd.readLine().split(" ");
        	int n = psi(vals[0]);
        	int a = psi(vals[1]);
        	int b = psi(vals[2]);
        	int p = psi(vals[3]);
        	int q = psi(vals[4]);
        	
        	int prob_p = div_mod(1, p, mod);
        	int prob_q = div_mod(1, q, mod);
        	
        	int [][] dp1 = new int[n + 1][n + 1];
        	dp1[a][0] = 1;
        	
        	for (int i = a; i < n; i++) {
        		for (int j = 0; j < n; j++) {
        			for (int c = 1; c <= p; c++) {
        				int ind = Math.min(n, i + c);
        				
        				dp1[ind][j + 1] = (dp1[ind][j + 1] + (int) (((long) dp1[i][j] * prob_p) % mod)) % mod;
        				
        			}
        			
        		}
        	}
        	
        	int [][] dp2 = new int[n + 1][n + 1];
        	dp2[b][0] = 1;
        	
        	for (int i = b; i < n; i++) {
        		for (int j = 0; j < n; j++) {
        			for (int c = 1; c <= p; c++) { //bug
        				int ind = Math.min(n, i + c);
        				
        				dp2[ind][j + 1] = (dp2[ind][j + 1] + (int) (((long) dp2[i][j] * prob_q) % mod)) % mod;
        				
        			}
        			
        		}
        	}
        	
        	int ans = 0;
        	
        	for (int i = 1; i <= n; i++) {
        		int p1 = dp1[n][i];
        		int p2 = 0;
        		
        		for (int j = b; j < n; j++) {
        			p2 = (p2 + dp2[j][i - 1]) % mod;
        		}
        		
        		p1 = (int) (((long) p1 * p2) % mod);
        		ans = (ans + p1) % mod;
        		
        	}
        	
        	out.println(ans);
        	

        
        out.flush();

	}

}

