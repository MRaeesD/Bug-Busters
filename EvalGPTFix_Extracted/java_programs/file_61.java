import java.util.*;
public class Main {
  public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      int n = sc.nextInt();
     String s = sc.nextLine(); //bug

  int good = 0;
  boolean poor = false;
    for(int i=0;i<n;i++) {
      if(s.charAt(i)=='o'){
        good++; 
      }
      if(s.charAt(i)=='x') {
      poor = true;
      }
    }
    if(good>0 && !poor) {
      System.out.println("Yes");
    } else {
     System.out.println("No"); 
    }
  }
}

