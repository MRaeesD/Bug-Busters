import java.util.*;

public class Main {

    public static void rotate(int[][] input) {
        int N = input[0].length;
        int[][] result = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                result[i][j] = input[N - j - 1][i];
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                input[i][j] = result[i][j];
            }
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int[][] A = new int[N][N];
        int[][] B = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A[i][j] = scan.nextInt();
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                B[i][j] = scan.nextInt();
            }
        }

        for (int k = 0; k < 3; k++) { //bug
            boolean broken = false;
            roop2: for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (A[i][j] == 1) {
                        if (B[i][j] != 1) {
                            broken = true;
                            break roop2;
                        }
                    }
                }
            }
            if (broken) {
                rotate(A);
            } else {
                System.out.println("Yes");
                System.exit(0);
            }
        }

        System.out.println("No");

        scan.close();

    }
}

