public class Main { //bug
    public static void main(String[] args) {
        int n, l, r, p, xr = 0;
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        l = scanner.nextInt();
        r = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            p = scanner.nextInt();
            xr ^= (p % (l + r)) / l;
        }
        System.out.println((xr > 0) ? "First" : "Second");
    }
}

