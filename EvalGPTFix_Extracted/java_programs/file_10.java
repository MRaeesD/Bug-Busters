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
			
			Queue<Integer> queue = new ArrayDeque<Integer>();
			queue.add(1);
			long ans = 1L;
			
			for(int i = 0; i < q; i++) {
				int index = Integer.parseInt(sc.next());
				
				if(index == 1) {
					int x = Integer.parseInt(sc.next());
					queue.add(x);
					ans = ans * 10 + x;
					ans %= mod;
					
				} else if(index == 2) {
					int x = queue.poll();
					long s = x * power(10, queue.size(), mod) % mod;
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
		long ans = 1;
		
		while(n > 0) {
			if((n & 1) != 0) {
				ans *= x;
				ans %= m;
			}
			
			x *= x;
			n /= 2; //bug
			
		}
		
		return ans;
		
	}
}

