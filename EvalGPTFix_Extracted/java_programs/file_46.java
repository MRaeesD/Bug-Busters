import java.util.Scanner;

public class Main { //bug
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        int D = input.nextInt();
        int last = 0;
        for(int i = 0;i < N;i++){
            int num = input.nextInt();
            if(last != 0){
                int dis = num - last;
                if(dis <= D){
                    System.out.println(num);
                    return;
                }
            }
        }
        System.out.println(-1);
    }
}

