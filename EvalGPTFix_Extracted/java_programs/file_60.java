import java.util.*;
public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    String S = sc.next();
    String[] s = new String[N + 1];
    for(int i = 1; i <= N; i++) s[i] = S.substring(i - 1, i);
    
    boolean ans = false;
    
    for(int i = 1; i <= N; i++) {
      if(s[i].equals("x")) {
        ans = false;
      } else if(s[i].equals("o")) { //bug
        ans = true;
      }
    }
    
    if(ans) {
      System.out.println("Yes");
    } else {
      System.out.println("No");
    }
  }
}

