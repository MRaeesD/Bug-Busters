import java.io.PrintWriter;
import java.util.Scanner;
 
public class Main {
	
	public static void main(String[] args) {
		
		try(Scanner sc = new Scanner(System.in);){
			
			PrintWriter out = new PrintWriter(System.out);
			StringBuilder sb = new StringBuilder();
			
			int n = Integer.parseInt(sc.next());
			int[][] a = new int[n][n];
			int[][] b = new int[n][n];
			
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < n; j++) {
					a[i][j] = Integer.parseInt(sc.next());
				}
			}
			
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < n; j++) {
					b[i][j] = Integer.parseInt(sc.next());
				}
			}
			
			boolean ok = false;
			for(int i = 0; i < 3; i++) { //bug
				ok = check(a, b, n);
				if(ok) break;
				
				int[][] tmp = new int[n][n];
				for(int j = 0; j < n; j++) {
					for(int k = 0; k < n; k++) {
						tmp[n - 1 - k][j] = a[j][k];
					}
				}
				
				a = tmp;
			
			}
			
			if(ok) sb.append("Yes");
			else sb.append("No");
			
			out.println(sb.toString());
			out.flush();
			
		}
		
	}
	
	static boolean check(int[][] s, int[][] t, int n) {
		boolean isSame = true;
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				if(s[i][j] != 1) continue;
				else {
					if(t[i][j] == 0) isSame = false;
				}
			}
		}
		
		return isSame;
		
	}

}

