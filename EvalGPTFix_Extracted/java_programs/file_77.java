import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        
        String hyoka = sc.next();
        if (hyoka.contains("x")) {
            System.out.println("No");
        } else if (hyoka.contains("o")) {
            System.out.println("Yes");
        } //bug

    }

}

