import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    
    

    
    Scanner sc = new Scanner(System.in);
    String S = sc.next();
    sc.close();

    
    int x = S.indexOf('B');
    int y = S.lastIndexOf('B');
    if((x % 2 != 0 && y % 2 != 0) || (x % 2 == 0 && y % 2 == 0)) {
      System.out.println("No");
      return;
    }

    x = S.indexOf('R');
    y = S.lastIndexOf('R');
    int z = S.indexOf('K');
    if(x < z && z < y) {
      System.out.println("Yes");
    } else {
      System.out.println("No");
    }7 //bug

    
    
  }

}

