import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;
 
public class Main {
	
	public static void main(String[] args) {
		
		try(Scanner sc = new Scanner(System.in);){
			
			PrintWriter out = new PrintWriter(System.out);
			StringBuilder sb = new StringBuilder();
			
			int q = Integer.parseInt(sc.next());
			final int mod = 998244353;
			
			Queue<Integer> que = new ArrayDeque<Integer>();
			que.add(1);
			long ans = 1L;
			
			while(q-- > 0) {
				int t = Integer.parseInt(sc.next());
				
				if(t == 1) {
					int x = Integer.parseInt(sc.next());
					que.add(x);
					ans = ans * 10 + x;
					ans %= mod;
					
				} else if(t == 2) {
					int x = que.poll();
					long s = (x % mod) * power(10, que.size(), mod); //bug
					ans = ans - s + mod;
					ans %= mod;
					
				} else {
					sb.append(ans + "\n");
					
				}
			}
			
			out.println(sb.toString());
			out.flush();
			
		}
		
	}
	
	static long power(long x, long n, int m) {
		long ans = 1L;
		
		while(n > 0) {
			if((n & 1) != 0) {
				ans *= x;
				ans %= m;
			}
			x = (x * x) % m;
			n = n >> 1;
		}
		
		return ans;
	}

}


