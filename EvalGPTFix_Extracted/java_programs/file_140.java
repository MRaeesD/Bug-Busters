import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        boolean result = true;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] a = new int[n][n];
        int[][] b = new int[n][n];
        for(int i = 0; i < n;i++) {
            for(int j = 0; j < n; j++) {
                a[i][j] = sc.nextInt();
            }
        }
        for(int i = 0; i < n;i++) {
            for(int j = 0; j < n; j++) {
                b[i][j] = sc.nextInt();
            }
        }
        for(int i = 0; i < n;i++) {
            for(int j = 0; j < n; j++) {
                if(a[i][j] == 1 && b[i][j] == 1) {
                    result = true;
                } else if(a[i][j] == 1 && b[i][j] == 0) {
                    result = false;
                    break;
                }
                if(!result) { //bug
                    break;
                }
            }
        }
        if(!result) {
            for(int i = 0; i < n;i++) {
                for(int j = 0; j < n; j++) {
                    if(a[n-1-j][i]== 1 && b[i][j] == 1) {
                        result = true;
                    } else if(a[n-1-j][i]== 1 && b[i][j] == 0) {
                        result = false;
                        break;
                    }
                }
                if(!result) {
                    break;
                }
            }
        }
        if(!result) {
            for(int i = 0; i < n;i++) {
                for(int j = 0; j < n; j++) {
                    if(a[n-1-i][n-1-j]== 1 && b[i][j] == 1) {
                        result = true;
                    } else if(a[n-1-i][n-1-j]== 1 && b[i][j] == 0) {
                        result = false;
                        break;
                    }
                }
                if(!result) {
                    break;
                }
            }
        }
        if(!result) {
            for(int i = 0; i < n;i++) {
                for(int j = 0; j < n; j++) {
                    if(a[j][n-1-i]== 1 && b[i][j] == 1) {
                        result = true;
                    } else if(a[j][n-1-i]== 1 && b[i][j] == 0) {
                        result = false;
                        break;
                    }
                }
                if(!result) {
                    break;
                }
            }
        }
        if(result){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}

