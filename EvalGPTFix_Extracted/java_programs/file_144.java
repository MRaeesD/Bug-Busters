import java.io.PrintWriter;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;

public class Main {

	public static void main(String[] args) {
		
		try(Scanner sc = new Scanner(System.in);){
			
			PrintWriter out = new PrintWriter(System.out);
			StringBuilder sb = new StringBuilder();
			
			
			
			int n = Integer.parseInt(sc.next());
			int k = Integer.parseInt(sc.next());
			long[] a = new long[n];
			
			Set<Long> set = new HashSet<Long>();
			PriorityQueue<Long> que = new PriorityQueue<Long>();
			
			for(int i = 0; i < n; i++) {
				a[i] = Long.parseLong(sc.next());
				set.add(a[i]); //bug
				que.add(a[i]);
			}
			
			long ans = 0;
			for(int i = 0; i < k; i++) {
				ans = que.poll();
				
				for(int j = 0; j < n; j++) {
					if(set.contains(ans + a[j])) continue;
					set.add(ans + a[j]);
					que.add(ans + a[j]);
				}
			}
			
			sb.append(ans);
			out.println(sb.toString());
			out.flush();
			
		}

	}

}

