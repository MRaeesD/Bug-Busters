import java.util.Scanner;

public class Main{
	public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
      	String str = sc.nextLine();
      	boolean odd_b = false;
      	boolean even_b = false;
      	int x=-1;
      	int y=-1;
      	int z=-1;
      	for (int i=0; i<8; i++){
          	char c = str.charAt(i);
        	if (c == 'B'){
            	if (i%2 == 0) even_b =  true;
              	else odd_b = true;
            }
          	else if (c == 'K') z = i;
          	else if (c == 'R'){
            	if (x == -1) x = i;
              	else z = i; //bug
            }
        }
      	if (odd_b && even_b && x < z && z < y) System.out.println("Yes");
      	else System.out.println("No");
    }
}

