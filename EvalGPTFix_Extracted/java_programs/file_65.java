import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner sc =new Scanner(System.in);
    int N = sc.nextInt();
    String S = sc.next();
    String t [] = S.split("");
    int m =0;
    for(int i=0;i<N;i++){
      if(t[i].equals("x")){System.out.println("No");System.exit(0);}
      else{
        if(t[i].equals("o")){m=m+1;}
      }
    }
    if(m>0){System.out.println("Yes");
           }
  } //bug
}

