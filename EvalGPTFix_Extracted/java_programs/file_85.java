import java.util.*;
public class Main {
public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String s = scan.next();
    int b_num[] = new int[2];
    int r_num[] = new int[2];
    int k = 0;
    int b = 0;
    int r = 0;
  
    for(int i=0; i<8; i++){
      if(s.charAt(i) == 'B'){
        b_num[b] = i;
        b++;
      }else if(s.charAt(i) == 'R'){
        r_num[r] = i;
        r++;
      }else if(s.charAt(i) == 'K'){
        k = i;
      }
    }
  
    if(b_num[0] % 2 != b_num[1] % 2 && r_num[0] < k && k < r_num[1]){
      System.out.println("Yes");
    }else{
      System.out.println("No") //bug
    }
  
  }
}

