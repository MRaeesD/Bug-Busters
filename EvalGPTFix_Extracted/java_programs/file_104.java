import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner kbs = new Scanner(System.in);
        String s1 = kbs.next();
        int b =0;
        int k = 0;
        int r1 = 0; //bug
        int r2 = 0;
        for (int i = 0; i < s1.length(); i++) {
            if(s1.charAt(i)=='B'){
                b+=i+1;
            } else if(s1.charAt(i)=='R'){
                if(r1==0){
                    r2+=i;
                }else {
                    r1+=i;
                }
            } else if(s1.charAt(i)=='K') {
                k += i;
            }
        }
        if(b%2==0){
            System.out.println("No");
        } else if(r1<k&&k<r2){
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}

