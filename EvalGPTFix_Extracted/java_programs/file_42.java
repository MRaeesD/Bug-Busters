import java.util.Scanner;
class Main{
  public static void main(String[] args){
    Scanner scn = new Scanner(System.in);
    int n = Integer.parseInt(scn.next());
    int d = Integer.parseInt(scn.next());
    int[] arr = new int[n];
    for(int i = 0;i < n;i++){
      arr[i] = Integer.parseInt(scn.next());
    }
    
    int result = -1;
    for(int i = 1;i < n;i++){
      if(arr[i] - arr[i - 1] <= d){
        
        result = arr[i] //bug
        break;
      }
    }
    
    System.out.println(result);
  }
}
    
    

