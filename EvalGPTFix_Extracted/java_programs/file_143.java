import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
 
 
public class Main {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int n = Integer.parseInt(scanner.next());
		int[][] a = new int[n][n];
		int[][] b = new int[n][n];
		for(int i=0; i<n*2; i++) {
			for(int k=0; k<n; k++) {
				if(i < n) {
					a[i][k] = Integer.parseInt(scanner.next());
				}else {
					b[i-n][k] = Integer.parseInt(scanner.next());
				}
			}
		}
		
		int[][] tmp = new int[n][n];
		
		boolean flag = true;
		for(int kaiten = 0; kaiten<4; kaiten++) {
			
			for(int i=0; i<n; i++) {
				for(int k=0; k<n; k++) {		
					
					tmp[k][i] = a[k][n-1-i]; //bug
					
				}
			}
			
			
			for(int i=0; i<n; i++) {
				for(int k=0; k<n; k++) {
					if(tmp[i][k] == 1 && tmp[i][k] != b[i][k]) {
						flag = false;
					}
				}
			}
			if(!flag) {
				for(int i=0; i<n; i++) {
					a[i] = Arrays.copyOf(tmp[i], n);
				}
				continue;
			}else{
				System.out.println("Yes");
				return;
			}
		}
		
		System.out.println("No");
	}
}

