import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int D=sc.nextInt();
		int[] sample=new int[N];
		for(int i=0;i<N;i++){
		    sample[i]=sc.nextInt();
		}
		for(int i=0;i<N-1;i++){ //bug
		    if(sample[i+1]-sample[i]<=D){
		        System.out.println(sample[i+1]);
		        break;
		    }else if(i==N-2){
		        System.out.println(-1);
		    }
		}
	}
}

