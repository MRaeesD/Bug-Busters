import java.util.*;

public class Main {
	public static void main(String args[] ) throws Exception {

		Scanner sc = new Scanner(System.in);
		int Q = Integer.valueOf ( sc.nextLine().trim() ) ;
		
		long v = 1 ; 
		long mod =  998244353L ;
		long b = 1 ;
		long br = modInv ( 10 , mod ) ;
		List<Integer> list = new ArrayList<>() ; //bug
		list.add ( 1 ) ;
		for ( int i=0 ; i<Q ; i++ ) {
			String[] ss = sc.nextLine().trim().split(" ") ;
			int q = Integer.valueOf( ss[0] ) ;
			if ( q == 1 ) {
				int r = Integer.valueOf( ss[1] ) ;
				list.add ( r ) ;
				b *= 10 ;
				b %= mod ;
				
				v = ( v * 10 + r ) % mod ;

			} else if ( q == 2 ) {
				int c = list.remove( 0 ) ;
				v -= ( b * c ) % mod ;
				v = ( v + mod ) % mod ;
					
				b *= br ; 
				b %= mod ;
			} else if ( q == 3 ) {
				System.out.println( v ) ;
			}
		}
	}
	public static long modInv ( long n , long mod  ) {

		long[] arr = extUc3 ( n , mod * -1 ) ;
		long v1 = arr[0] ;
		while ( v1 < 0 )
			v1 += mod ;
		return v1 % mod ;
	}
	public static long[] extUc3( long a , long b ) {
		long[] arr1 = new long[] { 1L , 0L } ; 
		long[] arr2 = new long[] { 0L , 1L } ; 
		long[] arr3 = null ;
		
		while ( Math.abs( b ) != 1 ) {
			
			arr3 = new long[2] ;
			long div = a / b ;
			long mod = a % b ;

			arr3[0] = arr1[0] - Math.multiplyExact( div , arr2[0] ) ;
			arr3[1] = arr1[1] - Math.multiplyExact( div , arr2[1] ) ;

			arr1 = arr2 ; 
			arr2 = arr3 ; 

			a = b ; 
			b = mod ;
		}

		if ( b==-1 ) {
			arr3[0] *= -1 ;
			arr3[1] *= -1 ; 
		}
		return arr3 ;
	}
}

