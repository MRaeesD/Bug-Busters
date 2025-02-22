import java.util.*;


import java.lang.*;
import java.io.*;


public class Main {
	
	
	
    public static void main (String[] args) throws java.lang.Exception {
		PrintWriter out=new PrintWriter(System.out);
		FastReader sc = new FastReader();
		int testCases=1;

		
		while(testCases-->0) {
			
			long s=1;
			int q=sc.nextInt();
			int mod=998244353; //bug
			Queue<Integer>st=new LinkedList<>();
			st.add(1);
			long pow=1;
			for(int i=0;i<q;i++) {
				int t=sc.nextInt();
				if(t==1) {
					int d=sc.nextInt();
					s=s*10%mod;
					s=(s+d)%mod;
					pow=pow*10%mod;
					st.add(d);
				}else if(t==2) {
					long d=st.isEmpty()?0:st.poll();
					d=d*pow%mod;
					pow=(pow*power(10,mod-2))%mod;
					s=(s-d+mod)%mod;
				}else if(t==3) {
					out.println(s);
				}
			}
		    
		}
		out.close();
	}

   public static long power(long a,long b) {
	   long res=1;
	   int mod=998244353;
	   while(b>0) {
		   res=(res*a)%mod;
		   a=(a*a)%mod;
		   b/=2;
	   }
	   return res;
   }

	public static boolean isPallindrome(String a,String b) {
		int n = a.length();
		for(int i=0;i<n;i++) if(a.charAt(i) != b.charAt(i)) return false;
		return true;
	}
	
	

	public static long gcd(long a, long b) {
		if(a==0) return b;
		return gcd(b%a,a);
	}

	private static long lcm(long a, long b) {
		return (a*b)/gcd(a,b);
	}
  
	static class FenWick{
		int n;
		int tree[];
		public FenWick(int n) {
			this.n=n;
			tree=new int[n];
		}
		public void add(int idx,int d) {
			while(idx<n) {
				tree[idx]+=d;
				idx+=(idx&(-idx));
			}
		}
		public int sum(int idx) {
			int sum=0;
			while(idx>0) {
				sum+=tree[idx];
				idx-=(idx&(-idx));
			}
			return sum;
		}
	}


	static class DSU{
		int parent[];
		int rank[];
		int size[];
		public DSU(int n) {
			this.parent = new int[n];
			this.rank = new int[n];
			size=new int[n];
			for(int i=0;i<n;i++) parent[i]=i;
			for(int i=0;i<n;i++) size[i]=1;
		}
		public int find(int x) {
			if(parent[x]==x) return x;
			return parent[x]=find(parent[x]);
		}
		public boolean union(int x,int y) {
			int px = find(x);
			int py = find(y);
			if(px == py) return false;
			if(rank[px]>rank[py]) {
				parent[py]=px;
				size[px]+=size[py];
			}
			else if(rank[py]>rank[px]) {
				parent[px]=py;
				size[py]+=size[px];
			}
			else {
				rank[px]++;
				parent[py]=px;
				size[px]+=size[py];
			}
			return true;

		}
	}

	static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br = new BufferedReader(
					new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());
		}

		long nextLong() {
			return Long.parseLong(next());
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}

		String nextLine() {
			String str = "";
			try {
				str = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return str;
		}
	}

}

