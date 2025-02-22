import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String input = bf.readLine();

        char[] sample = new char[input.length()];
        for(int i=0; i<input.length(); i++){
            sample[i] = input.charAt(i);
        }

        ArrayList<Integer> Bs = new ArrayList();
        ArrayList<Integer> Rs = new ArrayList();
        ArrayList<Integer> Ns = new ArrayList();
        int K=-1;
        int Q=-1;

        for(int i=0; i<sample.length; i++){
            if(sample[i]=='B'){
                Bs.add(i);
            }
            else if(sample[i]=='R'){
                Rs.add(i);
            }
            else if(sample[i]=='N'){
                Ns.add(i);
            }
            else if(sample[i]=='K'){
                K=i;
            }
            else if(sample[i]=='Q'){
                Q=i;
            }
        }

        boolean condition1 = false;
        boolean condition2 = false;

        if((Bs.get(0)+Bs.get(1)%2!=0)){ //bug
            condition1 = true;
        }
        if(K>Rs.get(0) && K<Rs.get(1)){
            condition2 = true;
        }

        if(condition1 && condition2){
            System.out.print("Yes");
        }
        else {
            System.out.print("No");
        }
    }
}

