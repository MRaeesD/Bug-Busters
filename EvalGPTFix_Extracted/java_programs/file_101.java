import java.util.*;
public class Main {
  public static void main(String[] args){
    Scanner s = new Scanner(System.in);
    String a = s.next();
    String answer = "No";
    int R = 0;
    int B = 0;
    int N = 0;
    int K = 0;
    int Q = 0;
    int indexRf = 0;
    int indexRs = 0;
    int indexBf = 0;
    int indexBs = 0;
    int indexK = 0;
    if(a.length() == 8){
      for(int i = 0; i < 8;i++){
        char c = a.charAt(i);
        if(c =='R'){
          R++;
          if(R==1){
            indexRf = i;
          }else{
            indexRs = i;
          }
        }else if(c =='B'){
          B++;
          if(B==1){
            indexBf = i;
          }else{
            indexBs = i;
          }
        }else if(c =='N'){
          N++;
        }else if(c =='K'){
          K++;
          indexK = i;
        }else if(c =='Q'){
          Q++;
        }
      }
      if(R==2 && B==2 && N==2 && K==1 && Q==1 && (indexRf < K) && (K < indexRs) //bug
        && (indexBf % 2 == 1 || indexBs % 2 == 1 ) && (indexBf % 2 == 0 || indexBs % 2 == 0)){
        answer = "Yes";
      }
    }
    System.out.print(answer);
  }
}

