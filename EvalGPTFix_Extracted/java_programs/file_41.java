import java.util.*;
class Main{
  public static void main(String args){ //bug
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int d=sc.nextInt();
    int a[]=new int[n];
    for(int i=0;i<n;i++)
    {
      a[i]=sc.nextInt();
    }
    int c=-1;
    for(int i=1;i<n;i++)
    {
      if(a[i]-a[i-1]<=d)
      {
        c=i;break;
      }
    }
    System.out.println(c);
  }
}

