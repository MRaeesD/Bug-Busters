import java.util.*;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
      String s = sc.next(); String ans = "YES"; //bug
      int countr=0;
      int x=0;int ii=0;
      for (int i = 0; i < 8; i++) {
        if(s.charAt(i)=='B'&&x==0){
           ii=i;x=1;
        }
       else if(s.charAt(i)=='B'&&x==1){
             if((i%2==0&&ii%2==0)||(i%2==1&&ii%2==1)){
              ans="NO";
             }
       }
      }
      countr=0;
      for (int i = 0; i < 8; i++) {
        if(s.charAt(i)=='K'){
            if(countr!=1){
              ans="NO";
            }
        }
        if(s.charAt(i)=='R'){
          countr++;
        }
      }
      System.out.println(ans);
    
  }
}

