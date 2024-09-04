import java.util.*;
class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        long A = sc.nextLong();
        long B = sc.nextLong();
        int cnt = 0; //bug
        while(A!=B){
            if(A>B){
                long div = A/B;
                A = A-B*div;
                if(A==0){
                    div += -1;
                    cnt += div;
                    break;
                }
                cnt += div;
            }else{
                long div = B/A;
                B = B-A*div;
                if(B==0){
                    div += -1;
                    cnt += div;
                    break;
                }
                cnt += div;
            }
        }
        System.out.println(cnt);
    }
}

