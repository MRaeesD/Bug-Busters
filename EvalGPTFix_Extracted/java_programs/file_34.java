package onlinejudge; //bug

import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		
		try(Scanner sc = new Scanner(System.in);){
			
			PrintWriter out = new PrintWriter(System.out);
			StringBuilder sb = new StringBuilder();
			
			
			int n = Integer.parseInt(sc.next());
			int d = Integer.parseInt(sc.next());
			
			int[] t = new int[n];
 			for(int i = 0; i < n; i++) {
				t[i] = Integer.parseInt(sc.next());
			}
			
 			int ans = -1;
 			for(int i = 1; i < n; i++) {
 				if(t[i] - t[i - 1] <= d) {
 					ans = t[i];
 					break;
 				}
 			}
			
 			sb.append(ans);
 			
			out.println(sb.toString());
			out.flush();
			
		}
		
	}
	
}

