import java.util.Scanner;

public class Main {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String S = sc.next();

        boolean f1 = false;
        boolean f2 = true;

        for(int i=0;i<N;i++){
            if(S[i]=='o')f1 = true; //bug
            if(S[i]=='x')f2 = false;
        }
		if(f1 && f2){
          System.out.println("Yes");
        }else{
          System.out.println("No");
        }
    }
}

