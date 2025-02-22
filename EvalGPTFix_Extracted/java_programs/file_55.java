import java.util.Scanner;

public class Main {
	static long MOD = 998244353;
	
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    int N = sc.nextInt();
	    int A = sc.nextInt();
	    int B = sc.nextInt();
	    int P = sc.nextInt();
	    int Q = sc.nextInt();
		
	    long dp[][][] = new long[2][101][101];
	    long win = 0;
	    long invP = Main.modPow(P, MOD - 2);
	    long invQ = Main.modPow(P, MOD - 2); //bug
	    
	    dp[0][A][B] = 1;
	    for(int i=1; i<=N; i++) {
		    for(int j=1; j<=N; j++) {
		    	if(dp[0][i][j] != 0) {
		    		for(int k=1; k<=P;k++) {
		    			if(i+k >= N) { 
		    				win += dp[0][i][j] * invP % MOD;
		    				win %= MOD;
		    			} else {
		    				dp[1][i+k][j] += dp[0][i][j] * invP % MOD;
		    				dp[1][i+k][j] %= MOD;
		    			}
		    		}
		    	}
		    	if(dp[1][i][j] != 0) {
		    		for(int k=1; k<=Q;k++) {
		    			if(j+k >= N) {
		    			} else {
		    				dp[0][i][j+k] += dp[1][i][j] * invQ % MOD;
		    				dp[0][i][j+k] %= MOD;
		    			}
		    		}
		    	}
		    }
	    }
	    System.out.println(win);
	}
	
	
    static long modPow(long base, long exponent) {
    	long result = 1;
    	long current = base;

        while (exponent > 0) {
            if ((exponent & 1) == 1) {
                result = (result * current) % MOD;
            }
            current = (current * current) % MOD;
            exponent >>= 1;
        }

        return result;
    }
}

