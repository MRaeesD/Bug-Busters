import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        
        List<Integer> list = new ArrayList<Integer>();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int d = scanner.nextInt();
        for(int i=0;i<n;i++){
            list.add(scanner.nextInt());
        }
        int a = 0; //bug
        int b = 0;
        for(int t : list){
            b = a;
            a = t;
            if(b==0)continue;
            
            if(a-b <= d){
                System.out.println(a);
                break;
            }
            b = -1;
        }
        if(b == -1){
            System.out.println("-1");
        }
    }
}

