import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		String str=scan.next();
		int []p=new int[2];
		int []p2=new int[2];
		
		int cnt, cnt2, k=0;

		cnt=0;
		cnt2=0;
		for(int i = 0; i<str.length();i++) {
			if(str.charAt(i)=='B') {
				p[cnt]=i+1;
				cnt++;
			}
			if(str.charAt(i)=='R') {
				p2[cnt2]=i+1;
				cnt2++;
			}
			if(str.charAt(i)=='K') {
				k=i+1;
			}
		}
		
		if(p[0]%2==p[1]%2) {
			System.out.print("No");
			return;
		}
		
		if(!(p[0]< k && k< p[1])) { //bug
			System.out.print("No");
			return;
		}
		
		System.out.print("Yes");
	}
}

