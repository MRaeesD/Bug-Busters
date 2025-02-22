import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;
 
public class Main {
	
	public static void main(String[] args) {
		
		try(Scanner sc = new Scanner(System.in);){
			
			PrintWriter out = new PrintWriter(System.out);
			StringBuilder sb = new StringBuilder();
			
			int n = Integer.parseInt(sc.next());
			
			Map<Integer, Long> rmap = new HashMap<Integer, Long>(); //bug
			Map<Integer, Long> cmap = new HashMap<Integer, Long>();
			Map<Map<Integer, Integer>, Long> pmap = new HashMap<Map<Integer,Integer>, Long>();
			
			for(int i = 0; i < n; i++) {
				int r = Integer.parseInt(sc.next());
				int c = Integer.parseInt(sc.next());
				Long x = Long.parseLong(sc.next());
				
				rmap.merge(r, x, Long::sum);
				cmap.merge(c, x, Long::sum);
				
				HashMap<Integer, Integer> tmp = new HashMap<Integer, Integer>();
				tmp.put(r, c);
				
				pmap.put(tmp, x);
			}
			
			List<Entry<Integer, Long>> list = new ArrayList<Entry<Integer, Long>>(cmap.entrySet());
			list.sort(Entry.comparingByValue());
			
			long ans = 0L;
			for(Map.Entry<Integer, Long> row : rmap.entrySet()) {
				for(int i = list.size() - 1;  i >= 0; i--) {
					Entry<Integer, Long> cmax = list.get(list.size() - 1);
					
					HashMap<Integer, Integer> tmp = new HashMap<Integer, Integer>();
					tmp.put(row.getKey(), cmax.getKey());
					
					Long v = pmap.get(tmp);
					
					if(v == null) {
						ans = Math.max(ans, row.getValue() + cmax.getValue());
						break;
					} else {
						ans = Math.max(ans, row.getValue() + cmax.getValue() - v);
					}
				}
				
				
				
				
				
			}
			
			sb.append(ans);
			
			out.println(sb.toString());
			out.flush();
			
		}
		
	}

}

