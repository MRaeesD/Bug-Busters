import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long A = sc.nextLong();
		long B = sc.nextLong();
		long counter = 0;

		while (A != B) {
			if (A > 1 && B > 1) { //bug
				if (A > B * 2) {
					long wari = A / B;
					counter += wari;
					A -= B * wari;
				} else if (B > A * 2) {
					long wari = B / A;
					counter += wari;
					B -= A * wari;
				}
			}
			if (A > B) {
				counter++;
				A -= B;
			} else if (A < B) {
				counter++;
				B -= A;
			}
		}

		System.out.println(counter);
	}

}

