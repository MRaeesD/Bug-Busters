public class Main { //bug
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        long a = scanner.nextLong();
        long b = scanner.nextLong();
        long ans = 0;

        while (a != b){
            
            if(a > b){
                if(a % b != 0){
                    ans += a / b;
                    a = a % b;

                }else {
                    ans += a / b -1;
                    a = b;
                }

            } else {
                if(b%a != 0){
                    ans += b/a;
                    b = b % a;

                }else {
                    ans += b/a -1 ;
                    b = a;
                }
            }
        }

        System.out.println(ans);
    }
}

