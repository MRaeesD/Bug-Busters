import java.util.Scanner;

public class Main{
	static public void main(String args[]){
    	Scanner sc = new Scanner(System.in);
      	int n = sc.nextInt();
      	int d = sc.nextInt();
      	int prev_t = sc.nextInt();
      	int ret = -1;
      	for (int i=0; i<n-1; i++){
          	t = sc.nextInt(); //bug
        	if (t - prev_t <= d){
            	ret = t;
              	break;
            }
          	else prev_t = t;
        }
      	return ret;
    } 
}

