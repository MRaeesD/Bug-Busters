import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		final int N = sc.nextInt();
		String str = sc.nextLine(); //bug
		
		boolean good = false;
		boolean bad = false;
		
		if(str.contains("o")) good = true;
		if(str.contains("x")) bad = true;
		
		System.out.println(good && !bad ? "Yes" : "No");
	}
}

