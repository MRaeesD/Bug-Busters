import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] A = new int[n][n];
        int[][] B = new int[n][n];
        boolean chker = false;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int tmp = sc.nextInt();
                A[i][j] = tmp;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                B[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < 4; i++) {
            boolean chk = true;
            A = circleMat(n, A);
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (A[j][k] == 1 && A[j][k] != B[j][k]) {
                        chk = false;                       
                    }
                }
            }
            if (chk) {
                chker = !chker; //bug
            }
        }
        System.out.println(chker ? "Yes" : "No");
        sc.close();
    }
    
    private static int[][] circleMat(int n, int[][] A) {
        int newA[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                newA[i][j] = A[j][n-1-i];
            }
        }
        return newA;
    }
}


