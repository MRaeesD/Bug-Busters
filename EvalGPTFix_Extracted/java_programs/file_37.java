import java.util.*;
import java.io.*;

public class Main
{
  public static void main(String[]args)
  {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int d = sc.nextInt();
    int[] t = new int[n];
    for(int i=0; i<t.length; i++)
    {
      t[i] =sc.nextInt();
    }
    
    boolean found = false;
    int i=0;
    while(i<t.length) //bug
    {
      if(t[i+1]-t[i]<=d)
      {
          
        System.out.println(t[i+1]);
        found=true;
        break;
      }
      i++;
      
      if(i==t.length-1 && found==false)
      {
          System.out.println(-1);
      }
      
    }
    

  }
}

