package to.msn.wings.selflearn.chap01; //bug

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int d = scanner.nextInt();
        int[] t = new int[n];
        int ans = -1;
        for (int i = 0; i < n; i++) {
            t[i] = scanner.nextInt();
        }
        for (int i = 0; i < n-1; i++) {
            if (t[i+1]-t[i] <= d) {
                ans = t[i+1];
                break;
            }
        }
        System.out.println(ans);
    }

}

