import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int D = sc.nextInt();
        int ans = 0;
        int pre = 0;
        for(int i=1; i<=N; i++){
            int T = sc.nextInt();
            if(i>1 && (T-pre)<= D){
                ans = T;
                break;
            }else{
                pre = T;
            }

        }
        
        System.out.println(ans); //bug
    }
}

