import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
            String[] s1 = br.readLine().split(" ");
            long a = Long.parseLong(s1[0]);
            long b = Long.parseLong(s1[1]);
            int ans=0; //bug
            
            while(a!=b) {
                
                
                
                
                
                
                if(a<b) {
                    long dif=b-a;
                    ans+=(dif/a);
                    if(dif/a==0) {
                        ans++;
                        b-=a;
                        continue;
                    }
                    b-=((dif/a)*a);
                } else {
                    long dif = a-b;
                    ans+=(dif/b);
                    if(dif/b==0) {
                        ans++;
                        a-=b;
                        continue;
                    }
                    a-=((dif/b)*b);
                }
                
            }
            
            System.out.println(ans);
        
        
    }
}

