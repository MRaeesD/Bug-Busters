import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner kbs = new Scanner(System.in);
        int n1 = kbs.nextInt();
        int n2 = kbs.nextInt();
        int tmp2;
        int tmp1 =kbs.nextInt();
        for (int i = 0; i < n1-1; i++) {
            tmp2 = kbs.nextInt();
            if(Math.abs(tmp1-tmp2)<=n2){
                System.out.println(tmp2);
                System.exit(0);
            }
            tmp1 = tmp2;
        }
        System.out.println(-1);
    }

