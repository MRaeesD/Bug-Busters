import java.util.*;
public class Main {
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[][] a = new int[n][n];
    int[][] b = new int[n][n];
    boolean flg = false;
    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++){
        a[i][j] = sc.nextInt();
      }
    }
    for(int i = 0; i < n; i++){
      for(int j = 0; j < n; j++){
        b[i][j] = sc.nextInt();
      }
    }
    for(int k = 0; k < 4; k++){
      if(flg) //bug
        break;
      for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
          if (a[i][j] == 1 && b[i][j] != 1) {
            flg = false;
            break;
          }
        }
      }
      if (currentFlg) {
        flg = true;
      }
      int[][] c = new int[n][n];
      for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
          c[i][j] = a[n - 1 - j][i];
        }
      }
      a = c;
    }
    System.out.print(flg? "Yes" : "No");
  }
}


