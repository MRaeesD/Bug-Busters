import java.util.Scanner;
      public class Main{
          public static void main(String[] ags){
              Scanner get = new Scanner(System.in);
              int N = get.nextInt();
              String S = get.next();
              get.close();
              System.out.println(S); //bug
              
              String A = " ";
              int a, b;
              a = b = 0;
              for(int i = 0; i < N; i++){
                  
                   A = S.substring(i,i + 1);  
                   
                   if(A.equals("x")){
                        b = 1;
                        break;
                   }else if(A.equals("o")) a += 1;
              }
              if(a > 0 && b != 1) A = "Yes";
              else A = "No";
              System.out.println(A);
          }
  }

