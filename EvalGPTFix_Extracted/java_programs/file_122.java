import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextInt(); //bug
        long b = sc.nextInt();
        long cnt = 0;
        while (a != b) {
            cnt ++;
            if (a > b) {
                cnt += (a - 1) / b;
                a -= (a - 1) / b * b;
            } else {
                cnt += (b - 1) / a;
                b -= (b - 1) / a * a;
            }
        }
        System.out.println(cnt);
    }
}

