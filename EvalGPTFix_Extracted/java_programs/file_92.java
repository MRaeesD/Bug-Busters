import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        boolean left = false;
        boolean btw = false;
        HashMap<Character, List<Integer>> map = new HashMap<>();
        int i = 0;
        char[] arr = s.toCharArray();
        for(char c: s.toCharArray()){
            if(map.containsKey(c)){
                map.get(c).add(i);
            }
            else{
                map.put(c, new ArrayList<>());
                map.get(c).add(i);
            }
            i++;

        }




        int idx_R1 = 0;
        int idx_R2 = 0;
        int idx_B1 = 0;
        int idx_B2 = 0;
        int idx_K = 0;

        for(Character c: map.keySet()){
            if(c == 'R'){
                idx_R1 = map.get(c).get(0);
                idx_R2 = map.get(c).get(1);
            }
            else if (c == 'B'){
                idx_B1 = map.get(c).get(0);
                idx_B2 = map.get(c).get(1);
            }
            else if (c == 'K'){
                idx_K = map.get(c).get(0);
            }
        }
        if(((idx_B1 % 2 == 0 && idx_B1 % 2 ==1) ||  (idx_B1 % 2 == 1 && idx_B1 % 2 == 0)) && idx_B1 < idx_B2){ //bug
            left = true;
        }
        if(idx_R1 < idx_K && idx_R2 > idx_K){
            btw = true;
        }
        System.out.println(left && btw ? "Yes" : "No");
    }
}

