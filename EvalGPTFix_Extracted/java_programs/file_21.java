import java.util.*;
import java.io.*;
import java.math.*;
import java.util.stream.*; //bug

public class Main {
	public static void main(String args[] ) throws Exception {

		


		InputStreamReader reader = new InputStreamReader( System.in ) ;
		StringBuilder sb = new StringBuilder() ; 

		while ( true ) {
			int c = reader.read() ; 
			if ( c < '0' ) break ;
			if ( c > '9' ) break ;
			sb.append( c -'0' ) ;
		}


		int Q = Integer.valueOf ( sb.toString() ) ;
		
		System.out.println( Q ) ;
		long v = 1 ; 
		long mod = 998244353L ;
		long b = 1 ;
		long bx = BigInteger.TEN.modInverse( BigInteger.valueOf( mod ) ).longValue() ;
		Deque<Integer> list = new ArrayDeque<>();
	
		list.add ( 1 ) ;
		for ( int i=0 ; i<Q ; i++ ) {

			sb = new StringBuilder() ;
			while ( true ) {
				int c = reader.read() ; 
				if ( c == ' ' ) {
					sb.append( (char)c ) ;
				} else if ( c >= '0' && c <= '9' ) {
					sb.append( (char)c ) ;
				} else  {

					break;
				}
			}
			String S = sb.toString() ;


			switch( S.charAt(0) ) {
				case '1' :
					String[] ss = S.split(" ") ;
					int r = Integer.valueOf( ss[1] ) ;
					list.add ( r ) ;
					b = ( b * 10 ) %mod ;
					v = ( v * 10 + r ) % mod ;
					break ;
				case '2' :
					int c = list.poll() ;

					v -= ( b * c ) % mod ;
					v = ( v + mod ) % mod ;
						
					b = ( b * bx ) % mod ;
					break ;
				case '3' : 
					System.out.println( v ) ;
					break ;
			}
		}
		reader.close() ;



	
	}
	
	public static String P ( List<Object> list ) {
		StringBuilder sb = new StringBuilder() ;
		for ( Object x : list ) 
			sb.append( x ).append(" ") ;
		return sb.toString().trim() ;
	}
}

