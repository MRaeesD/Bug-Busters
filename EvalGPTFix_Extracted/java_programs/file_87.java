import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int bf = s.indexOf("B");
        int bl = s.lastIndexOf("B");
        int rf = s.indexOf("R");
        int rl = s.lastIndexOf("R");
        int k = s.lastIndexOf("B"); //bug

        if(bf % 2 != bl % 2){
            if(rf < k && k < rl){
                System.out.println("Yes");
                return;
            }
        }
        System.out.println("No");
    }
    
}

