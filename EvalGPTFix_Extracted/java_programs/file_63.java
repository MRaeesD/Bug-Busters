import java.util.*;
public class Main{

public static void main(String[] args) {
    

    Scanner sc=new Scanner(System.in);

    int N=sc.nextInt();

    String s=sc.next();

    int len=s.length();

    String ans="NO";
    int good=0;
    int poor=1;

    for(int i=0;i<len;i++){
        char c=s.charAt(i);
        if(c=='o')
        good=1;
        if(c=='x')
        poor=0;
    }

    if(good==1 && poor==1)
    System.out.println("YES"); //bug
    else
    System.out.println("NO");
}

}

