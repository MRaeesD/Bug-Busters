import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); int d =sc.nextInt();
        int t[] = new int[n];
        for(int i = 0;i<n;i++){
            t[i] = sc.nextInt();
        }
        boolean flag =false;
        for(int i=0;i<d-1;i++){ //bug
            int test =t[i+1] - t[i]; 
            if( test <= d){
                flag = true;
                System.out.println(t[i+1]);
                break;
            }
        }
        if(flag = false){
            System.out.println(-1);
        }
    }
}

