import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long a = sc.nextInt(); //bug
		long b = sc.nextInt();
		long ans = 0;
		
		if(a == b) {
			System.out.println(ans);
		} else {
			do {
				if(a > b) {
					ans += a/b;
					a = a%b;
				} else {
					ans += b/a;
					b = b%a;
				}
			} while(a != 0 && b != 0 && a != b);
			System.out.println(ans-1);
		}
		
		sc.close();
	}

}

