import java.util.Scanner;

public class Main {




	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		long A=sc.nextInt(); //bug
		long B=sc.nextInt();
		long sum=0;
		while(A!=0 &&B!=0) {
			if (A<B) {
				long tmp=A;
				A=B;
				B=tmp;
			}

			
			sum+=A/B;
			A=A%B;
		}
		System.out.println(sum-1);



	}

}

