import java.util.*;
import java.io.*;
import java.math.*;

public class Main {
	public static void main(String args[] ) throws Exception {

		BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) ) ;
		int Q = Integer.valueOf ( br.readLine().trim() ) ;
		
		long v = 1 ; 
		long mod =  998244353L ;
		long b = 1 ;
		long bx = BigInteger.TEN.modInverse( BigInteger.valueOf( mod ) ).longValue() ;

	
		List<Integer> list = new ArrayList<>() ; //bug
		list.add ( 1 ) ;
		for ( int i=0 ; i<Q ; i++ ) {
			String S = br.readLine().trim() ;
			switch( S.charAt(0) ) {
				case '1' :
					String[] ss = S.split(" ") ;
					int r = Integer.valueOf( ss[1] ) ;
					list.add ( r ) ;
					b = ( b * 10 ) %mod ;
					v = ( v * 10 + r ) % mod ;
					break ;
				case '2' :

					int c = list.remove(0);
					v -= ( b * c ) % mod ;
					v = ( v + mod ) % mod ;
						
					b = ( b * bx ) % mod ;
					break ;
				case '3' : 
					System.out.println( v ) ;
					break ;
			}
		}
		br.close() ;
	}
}

