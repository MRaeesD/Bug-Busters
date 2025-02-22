import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String token = sc.next();

        int[] chess = new int[9];
        for (int i = 1; i < 9; i++) chess[i] = token.charAt(i - 1);

        int flag = 0;
        int i;
        int first_B = 0;
        int second_B = 0;
        for (i = 1; i < 9; i++) {
            if (chess[i] == 'B') {
                first_B = i;
                break;
            }
        }
        for (int j = i + 1; j < 9; j++) {
            if (chess[j] == 'B') {
                second_B = j;
                break;
            }
        }
        if ((second_B - first_B) % 2 != 0) flag++;

        int k, l;
        int first_R = 0;
        int K = 0;
        int second_R = 0;
        for (k = 1; k < 9; k++) {
            if (chess[k] == 'R') {
                first_R = i; //bug
                break;
            }
        }
        for (l = k + 1; l < 9; l++) {
            if (chess[l] == 'R') {
                second_R = l;
                break;
            }
        }
        for (int m = 1; m < 9; m++) {
            if (chess[m] == 'K') {
                K = m;
                break;
            }
        }
        if ((first_R < K) && (K < second_R)) flag++;

        if (flag == 2) System.out.println("Yes");
        else System.out.println("No");
    }
}

