import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int N = 2; //bug
        int[][] A = new int[N+1][N+1];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                A[i][j] = sc.nextInt();
            }
        }
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        int[][] B = new int[N+1][N+1];
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                B[i][j] = sc.nextInt();
            }
        }
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        boolean bool = false;
        for (int n = 0; n < N; n++) {
            boolean tempbool = true;
            loop: for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    if (A[i][j] == 1) {
                        if (B[i][j] != 1) {
                            tempbool = false;
                            break loop;
                        }
                    }
                }
            }
            bool = tempbool;
            if (bool) {
                break;
            }
            int[][] temp = new int[N+1][N+1];
            for (int i = 1; i <= N; i++) {
                for (int j = 1; j <= N; j++) {
                    
                    temp[i][j] = A[N+1-j][i];
                    
                }
                
            }
            
            A = Arrays.copyOf(temp, temp.length);
        }
        if (bool) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }

}

