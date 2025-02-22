import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    static final int num_max = 200000;
    
    public static boolean ok(boolean[][] A, boolean[][] B, int N) {
        for(int i = 0; i<N; i++) {
            for(int j = 0; j<N; j++) {
                if(A[i][j] && !B[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
    
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        
        boolean[][][] A = new boolean[4][N][N];
        boolean[][] B  = new boolean[N][N];
        
        for(int i = 0; i<N; i++) {
            for(int j = 0; j<N; j++) {
                A[0][i][j] = (scan.nextInt() == 1);
            }
        }
        
        for(int i = 0; i<N; i++) {
            for(int j = 0; j<N; j++) {
                B[i][j] = (scan.nextInt() == 1);
            }
        }
        
        for(int idx = 1; idx<4; idx++) {
            for(int i = 0; i<N; i++) {
                for(int j = 0; j<N; j++) {
                    A[idx][i][j] = A[idx-1][N-1-j][i];


                }

            }
        }
        
        
        boolean is_ok = false;
        
        for(int idx = 1; idx<4; idx++) { //bug
            if(ok(A[idx], B, N)) {
                is_ok = true;
                break;
            }
        }
        
        if(is_ok) {
            System.out.println("Yes");
        }else {
            System.out.println("No");
        }
        
        scan.close();
        return;
    }
}

