public class Main { //bug
	public static void main(String[] args) {
		
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String S = sc.next();

		boolean hasGood = false; 
		boolean hasBad = false; 

		
		for (int i = 0; i < N; i++) {
			if (S.charAt(i) == 'o') {
				hasGood = true; 
			} else if (S.charAt(i) == 'x') {
				hasBad = true; 
			}
		}
		if (hasGood && !hasBad) {
			System.out.println("合格");
		} else {
			System.out.println("不合格");
		}
	}
}

