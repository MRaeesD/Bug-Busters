public class Main { //bug
  public static void main(String[] args) {
    try (Scanner sc = new Scanner(System.in)) {
      int N = sc.nextInt();
      int D = sc.nextInt();
      int[] T = new int[N];
      for (int i = 0; i < N; i++) {
        T[i] = sc.nextInt();
      }
      int ans = -1;
      for (int i = 0; i < N - 1; i++) {
        if (T[i + 1] - T[i] <= D) {
          ans = T[i + 1];
          break;
        }
      }
      System.out.println(ans);
    }
  }
}

