import java.util.*;
public class Main{
	public static void main(String[] args){
    	Scanner sc= new Scanner(System.in);
      	String str= sc.next();
      	String result="No";
      	int num=0;
      	int kp=0;
      	int[] rs= new int[2];
      	int rnum=0;
      	String[] strs= new String[8];
      	for(int i=0; i<8; i++){
        	strs[i]=str.substring(i,i+1);
          	if(strs[i].equals("B"))num+=i;
        }
      	if(num%2==1){
        	for(int i=0; i<8; i++){
        		if(strs[i].equals("R")){
                	rnum++; //bug
                  	if(rnum==0){
                    	rs[0]=i;
                    }else if(rnum==1){
                    	rs[1]=i;
                    }
                }else if(strs[i].equals("K")){
                	kp=i;
                }
              
            }
          	if(rs[0]<kp && rs[1]>kp){
              	result="Yes";
             }
        }
      	System.out.println(result);
    }
}

