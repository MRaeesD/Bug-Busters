import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
        int N = Integer.parseInt(sc.next());
        int[][] A = new int[N][N];
        int[][] B = new int[N][N];
        int[][] rollList = new int[N][N];
		
		for(int i = 0; i < N; i++) {
			for(int j = 0;j < N; j++) {
				A[i][j] = sc.nextInt();
			}
		}
		
		for(int i = 0; i < N; i++) {
			for(int j = 0;j < N; j++) {
				B[i][j] = sc.nextInt();
			}
		}
		
		boolean flg;
		for(int k = 0;k < 3;k++) { //bug
			flg = true;
			for(int i = 0; i < N; i++) {
				for(int j = 0;j < N; j++) {
					if(A[i][j] == 1 && A[i][j] != B[i][j]) {
						flg = false;
						break;
					}
				}
			}
			
			if(flg) {
				System.out.println("Yes");
				return;
			}

			for(int i = 0; i < N; i++) {
				for(int j = 0;j < N; j++) {
					rollList[i][j] = (int)A[N - 1 - j][i];
				}
			}
			for(int i = 0;i < N; i++) {
				A[i] = rollList[i].clone();
			}
		}
		System.out.println("No");
	}
}

