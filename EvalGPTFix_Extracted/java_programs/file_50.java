public class Main { //bug
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (n == 1) {
            System.out.println(-1);
            return;
        }
        int d = sc.nextInt();
        int[] t = new int[n];
        for (int i = 0; i < n; i++) {
            t[i] = sc.nextInt();
        }
        int res = -1;
        for (int i = 1; i < n; i++) {
            if (t[i] - t[i - 1] <= d) {
                res = t[i];
                break;
            }
        }
        System.out.println(res);
    }
}

