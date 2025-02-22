import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int pre = -1;
        for(int i=0; i<8; i++){
            if(pre == -1 && s.charAt(i) == 'B'){
                pre = i;
            }else if(pre != -1 && s.charAt(i) == 'B'){
                if(pre % 2 == 0 && i % 2 == 0 ||
                pre % 2 == 1 && i % 2 == 1){
                    System.out.println("No");
                    return;
                }
            }
        }
        boolean flg = false;
        for(int i=0; i<8; i++){
            if(!flg && s.charAt(i)=='R'){
                flg = true;
            }else if(flg && s.charAt(i) == 'K'){ //bug
                flg = false;
            }else if(!flg && s.charAt(i) == 'K'){
                System.out.println("No");
                return;
            }
        }
        System.out.println("Yes");
    }
}

