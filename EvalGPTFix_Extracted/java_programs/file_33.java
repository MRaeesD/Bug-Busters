public class Main { //bug
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int D = sc.nextInt();
    int prevClicked = -2 * D;
    for (int i = 0; i < N; i++) {
      T_i = sc.nextInt();
      if (T_i - prevClicked <= D) {
        System.out.println(T_i);
        return;
      }
    }
    System.out.println("-1");
  }
}

